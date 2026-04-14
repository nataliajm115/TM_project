# Default repository template

## Hype decay: temporal sentiment dynamics in multilingual fan discourse

## Abstract

hiii

Can you tell where a rapper is from just by reading their English lyrics? This project explores whether the native 
language of a bilingual rapper leaves subtle fingerprints in the English verses they write. We focus on rappers of (CHOOSE
LANGUAGES) native languages. We take a two-step approach: first we train the model on text corpora of non-native English
writing to then fine-tune it on English lyrics. We specifically target underground artists as they are less likely to 
have native English ghostwriters. Using classification we look for patterns that betray a rapper's roots unusual word 
choices, rhyme schemes that feel "off" in English, and other traces of a first language peeking through. The bigger 
question we're asking is: when you learn to rap in someone else's language, how much of your own do you bring with you?

## Research questions

1. Can the temporal evolution of fan sentiment on Reddit be used to classify album releases into distinct reception
archetypes (hype collapse, slow burn, stable love, polarised)?
2. What lexical and topical features characterize each archetype, and do early posts (first 48 hours) contain predictive
signals of long-term reception?
3. Do different language communities discussing the same album follow similar sentiment trajectories, or does hype
behave differently across cultures?
4. What aspects of an album does each language community foreground, and do these differ systematically?

## Dataset

Our primary data source is Reddit, accessed via the Pushshift archive (Arctic Shift API), which provides historical
posts and comments with timestamps, upvote counts, and full text. For each album in our corpus we collect all posts and
top-level comments from the relevant artist subreddit (e.g. r/Kanye, r/FrankOcean, r/KendrickLamar) in a window spanning
7 days before to 30 days after the release date. We estimate 500–15,000 comments per album depending on community size,
yielding a total corpus of approximately 50,000–100,000 documents.

## A tentative list of milestones for the project

Add here a sketch of your planning for the coming weeks. Please mention who does what.

## Documentation

This can be added as the project unfolds. You should describe, in particular, what your repo contains and how to reproduce your results.

