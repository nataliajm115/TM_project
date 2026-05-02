## Training Data: PELIC

We use the **Pittsburgh English Language Institute Corpus (PELIC)** as the training data for our Native Language Identification classifier.

### What is PELIC?

PELIC is a learner corpus of English written and spoken production by international students enrolled in the English Language Institute at the University of Pittsburgh. It was compiled between 2006 and 2019 from coursework collected across multiple proficiency levels and class types.

The compiled corpus contains **159,126 text samples** from learners spanning a range of native language (L1) backgrounds and proficiency levels. Each sample is annotated with:

- `anon_id` — anonymized student identifier (enables student-level data splits)
- `L1` — the student's native language (our prediction target)
- `level_id` — proficiency level
- `text` — the raw learner text
- `tokens`, `tok_lem_POS` — pre-tokenized and POS-tagged versions
- Additional metadata: course, class, question prompt, gender, semester, placement test scores

The corpus is publicly available at [github.com/ELI-Data-Mining-Group/PELIC-dataset](https://github.com/ELI-Data-Mining-Group/PELIC-dataset).

### Why PELIC for this project?

PELIC is well-suited as the **training set** for our cross-register NLI experiment for several reasons:

1. **Sufficient scale per L1.** With over 150K samples across multiple native languages, PELIC provides enough Spanish-L1 data to train a classifier that learns L1-specific transfer patterns rather than overfitting to individual writers.

2. **Student-level metadata.** The `anon_id` column allows us to split data at the student level (rather than the sample level), preventing data leakage where the same writer's texts appear in both training and evaluation sets.

3. **Proficiency annotations.** The `level_id` field lets us filter to intermediate-and-above writers, where L1 transfer effects are strong enough to be detectable but not so dominant that texts are unintelligible.

4. **Widely used in NLI research.** PELIC and its predecessor corpora (like the TOEFL11 corpus, the EFCAMDAT) are standard benchmarks in the NLI literature, making our results comparable to prior work (see Literature review).

### Citation

> Juffs, A., Han, N-R., & Naismith, B. (2020). *The University of Pittsburgh English Language Institute Corpus (PELIC)*. http://doi.org/10.5281/zenodo.3991977
