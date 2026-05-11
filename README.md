# Using NLP to Uncover Rappers' Linguistic Roots
Fela, Giorgia, Natalia, and Nico

## Abstract
Can you tell where a rapper is from just by reading their English lyrics? This project aims to explore whether a bilingual rapper leaves subtle traces of their native language in the English verses they write. We focus on rappers with Spanish, French, Italian, Russian, or Chinese as their native languages. We will limit ourselves to these Indo-European languages due to our own linguistic capacities and their relative abundance of tools within NLP.  We will take a two-step approach: first we train the model on text corpora of non-native English
writing to then fine-tune it on English lyrics. We specifically target underground artists because they are less likely to 
have native English ghostwriters. We will use classification to look for patterns that betray a rapper's roots like: unusual word 
choices, unconventional idiom usage, rhyme schemes that feel "off" in English, and other traces of a first language peeking through. Our background as students in a multi-lingual space that is dominated by English (the majority's second language) invites us to think about the influence of the language you are or aren't speaking on what you say and how this is precieved. The bigger question we're asking is: when you learn to rap and express yourself in someone else's language, how much of your own do you bring with you?

## Research questions

1. Can a classifier trained on non-native English writing corpora and fine-tuned on rap lyrics successfully identify a 
rapper's native language from their English verses alone?
2. Are some native language backgrounds more "detectable" than others in English rap, and if so, why?

## Dataset
- Soundcloud
- Genius lyrics
- Million Song Database http://millionsongdataset.com/
- University of Pittsburg (Arabic, Chinese, Japanese, Korean, Spanish, and Turkish)
https://eli-data-mining-group.github.io/Pitt-ELI-Corpus/
https://github.com/ELI-Data-Mining-Group/PELIC-dataset
- COREFL: Corpus of English as a Foreign Language (Spanish, Chinese, Czech, Estonian, German, French, Greek Italian, Turkish)
https://corefl.learnercorpora.com/search_simple


## A tentative list of milestones for the project
| Milestone                                              | Deadline              | Who     |
|--------------------------------------------------------|-----------------------|---------|
| README up with project plan                            | April 14              | All     |
| Finalize language classes & artist lists               | April 17              | Natalia |
| Data collection – language group 1 (SoundCloud/Genius) | April 21              | Natalia |
| Source & preprocess training text corpora              | April 21              | Natalia |
| **Project update 1**                                   | **April 24**          | **All** |
| Data cleaning, language filtering, verse segmentation  | April 10              | Natalia |
| Baseline model (SVM)                                   | May 10                | Fela    |
| Evaluation & error analysis                            | May 7                 | TBD     |
| **Project update 2**                                   | **May 12**            | **All** |
| Write report                                           | May 12–18             | All     |
| Prepare presentation slides                            | May 15–18             | All     |
| **In-class presentations**                             | **May 19/22**         | **All** |
| **Final submission**                                   | **May 22 23:59 CEST** | **All** |

## Documentation

### What this repo does

We train an SVM to predict a singer's first language (Spanish, Italian, or French) from their English-language lyrics, 
a Native Language Identification (NLI) task on song lyrics.

### Repository structure

- `build_lyrics_corpus_{spanish,italian,french}.ipynb`: corpus construction (Wikidata + MusicBrainz candidate discovery, Genius scraping, line-level English extraction via fastText)
- `data/combined/`: final corpora and train/eval splits
- `data/combined/combine_and_split.py`: combines per-L1 corpora and produces artist-level train/eval splits
- `SVM_NLI_TextMining.ipynb`: classifier training and evaluation
- `training_data.md`: corpus statistics

### Corpus

99 songs by 36 artists (63 Spanish / 24 Italian / 12 French), constructed by scraping Genius lyrics and extracting only 
English-classified lines via fastText (confidence ≥ 0.7). Split 80/20 at the artist level, 
stratified by L1, with `random_state=42`. See `training_data.md` for full statistics.

### Reproducing results

1. Add a Genius API token to `.env` (`GENIUS_TOKEN=...`)
2. Open `SVM_NLI_TextMining.ipynb` and run top to bottom

To rebuild the corpus from scratch (several hours), run the three `build_lyrics_corpus_*.ipynb` notebooks first, then 
`python data/combined/combine_and_split.py --input-dir data/combined --output-dir data/combined`.