"""
Combine per-L1 lyrics CSVs and produce train/eval splits for SVM-based NLI.

Inputs (expected in --input-dir, defaults to ./):
    english_extracted_corpus_spanish.csv
    english_extracted_corpus_italian.csv
    english_extracted_corpus_french.csv

Each input CSV must have at least: artist_slug, artist_name, song_id, title, text

Outputs (to --output-dir, defaults to ./):
    lyrics_combined.csv   — full corpus with `L1` column
    lyrics_train.csv      — ~80% of artists (per L1)
    lyrics_eval.csv       — ~20% of artists (per L1)

Splitting policy:
    Artist-level split, stratified by L1. No artist appears in both train and eval.
    This is critical for NLI — otherwise the SVM memorizes idiolect, not L1 signal.

Usage:
    python combine_and_split.py
    python combine_and_split.py --input-dir ./data --output-dir ./data --eval-frac 0.2
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

RANDOM_STATE = 42  # consistent with project conventions

L1_FILES = {
    "spanish": "english_extracted_corpus_spanish.csv",
    "italian": "english_extracted_corpus_italian.csv",
    "french":  "english_extracted_corpus_french.csv",
}


def load_and_tag(input_dir: Path) -> pd.DataFrame:
    frames = []
    for l1, fname in L1_FILES.items():
        path = input_dir / fname
        if not path.exists():
            print(f"  [WARN] {path} not found — skipping {l1}")
            continue
        df = pd.read_csv(path)
        # Normalize: some L1 corpora call the column 'english_only_text',
        # others call it 'text'. Coalesce into 'text'.
        if "english_only_text" in df.columns:
            if "text" in df.columns:
                df["text"] = df["text"].fillna(df["english_only_text"])
            else:
                df = df.rename(columns={"english_only_text": "text"})
            df = df.drop(columns=["english_only_text"], errors="ignore")
        df["L1"] = l1
        print(f"  {l1:8s}: {len(df):4d} songs, {df['artist_slug'].nunique():3d} artists")
        frames.append(df)
    if not frames:
        raise FileNotFoundError("No input CSVs found.")
    return pd.concat(frames, ignore_index=True)


def artist_stratified_split(df: pd.DataFrame, eval_frac: float, seed: int):
    """Split artists per L1, then assign all songs by each artist accordingly.

    Returns (train_df, eval_df, split_log_df).
    split_log_df records, per L1, how many artists/songs went to each split.
    """
    rng = np.random.default_rng(seed)
    train_parts, eval_parts, log_rows = [], [], []

    for l1, group in df.groupby("L1"):
        artists = np.array(group["artist_slug"].unique().tolist())
        rng.shuffle(artists)
        n_eval = max(1, int(round(len(artists) * eval_frac)))
        # Guard: leave at least one artist in train
        if n_eval >= len(artists):
            n_eval = len(artists) - 1
        eval_artists = set(artists[:n_eval])
        train_artists = set(artists[n_eval:])

        train_g = group[group["artist_slug"].isin(train_artists)]
        eval_g  = group[group["artist_slug"].isin(eval_artists)]
        train_parts.append(train_g)
        eval_parts.append(eval_g)

        log_rows.append({
            "L1": l1,
            "n_artists_total": len(artists),
            "n_artists_train": len(train_artists),
            "n_artists_eval":  len(eval_artists),
            "n_songs_train":   len(train_g),
            "n_songs_eval":    len(eval_g),
        })

    return (
        pd.concat(train_parts, ignore_index=True),
        pd.concat(eval_parts,  ignore_index=True),
        pd.DataFrame(log_rows),
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input-dir",  type=Path, default=Path("."))
    p.add_argument("--output-dir", type=Path, default=Path("."))
    p.add_argument("--eval-frac",  type=float, default=0.2)
    p.add_argument("--seed",       type=int,   default=RANDOM_STATE)
    args = p.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading per-L1 corpora:")
    combined = load_and_tag(args.input_dir)
    print(f"\nCombined: {len(combined)} songs, "
          f"{combined['artist_slug'].nunique()} artists, "
          f"{combined['L1'].nunique()} L1s")

    combined.to_csv(args.output_dir / "lyrics_combined.csv", index=False)
    print(f"Wrote: {args.output_dir / 'lyrics_combined.csv'}")

    print(f"\nArtist-level split (eval_frac={args.eval_frac}, seed={args.seed}):")
    train, eval_, log = artist_stratified_split(combined, args.eval_frac, args.seed)
    print(log.to_string(index=False))

    # Sanity check: no artist overlap
    overlap = set(train["artist_slug"]) & set(eval_["artist_slug"])
    assert not overlap, f"Artist leak between train and eval: {overlap}"
    print("✓ No artist overlap between train and eval")

    train.to_csv(args.output_dir / "lyrics_train.csv", index=False)
    eval_.to_csv(args.output_dir / "lyrics_eval.csv",  index=False)
    print(f"Wrote: {args.output_dir / 'lyrics_train.csv'} ({len(train)} songs)")
    print(f"Wrote: {args.output_dir / 'lyrics_eval.csv'}  ({len(eval_)} songs)")


if __name__ == "__main__":
    main()
