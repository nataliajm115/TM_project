# Default repository template

## Hype decay: temporal sentiment dynamics in multilingual fan discourse

## Abstract
This project investigates how fan discourse around major album releases evolves over time across multilingual online 
communities. Using Reddit and other platforms, we collect posts and comments in different languages 
surrounding 8–10 albums spanning 2016–2022, selected to represent distinct receptions. We apply sentiment analysis and 
topic modeling to track how opinion shifts from release day through the following month. As a secondary lens, 
we compare whether hype trajectories are consistent across language communities discussing the same album. Our findings 
aim to assess whether music hype is a global or a culturally specific phenomenon.

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