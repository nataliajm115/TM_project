# Global plan 
1. collect data (labeled learner corpus for a possible pre-trained model and labeled song lyrics for Logistic Regression model)
2. preprocess data (cleaning up, sorting, splitting off testing and evaluating parts)
3. make a SVM model based on song lyric data (helpful examples/guides for model architecture: Kulmizev and Perkins)
4. evaluate model
5. if not to standards: look into making it into an ensemble model with Logistic Regression
6. make and evaluate new model
7. if still not up to standards: look into creating a pre-trained model with BERT (helpful example/guide for model architecture: Tejas-Nanaware)
8. evaluate all models
9. make nice presentation with conclusions
10. yay!

## Literature review
When we take a look at the existing literature on Native Language Identification (from here on shortened to: NLI), we find that it was traditionally performed with the help of a Logistic Regression Classifier or a Support Vector Machine Classifier. These are sometimes combined into ensemble models to increase accuracy (Nie), but other studies conclude that the improvements in predictions are not worth the additional computable power required for ensemble models (Kulmizev et al.). These classifiers usually end up classifying data that was split of from the same data set they were trained on. Stehwien and Padó noted that many of these classifiers consequently are only well-suited to the data type they have been trained on (e.g. models trained on learner corpora only being able to correctly identify the native language of learner corpora), due to topic bias. This is why it might be attractive to work with a pre-trained model that is only fine tuned for the classification task with the target data. So, since the developments in the field of transformer models there have also been studies applying BERT and GPT models to NLI (Zhang and Salle) (Kramp et al.), which give higher accuracy rates, but requires bigger computing capacity and comes with their own set of problems (data leaking in the case of GPT models and sequence length restriction in the case of BERT). 

We did not yet find instances of other groups performing NLI on song lyrics, Learner Corpora (to further NLI for purposes in Second Language Aquisition) still seem to be the most popular data set, although we did find some people working on NLI as part of linguistic forensics in journalism.

For our project, we have decided it would be the best choice to go with the (albeit slightly outdated) Logistic Regression Classification method which uses a labeled data set of song lyrics we have collected (the same way that Perkins and Grant did with NLI on blogposts), because we feel that the computational power is most suited for our project scope, we do not want to risk data leaking (and all our data is readily available on the internet), it is generally considered to be one of the more interpretable models, which is especially value able for tasks like NLI which might have other variables at play, like multiple languages influencing the L2 output. We will experiment with different parameters, the effect of making our model into an ensemble model and with the difference between character n-grams and word n-grams. If we end up being very disappointed with the performance of these models, we could look into creating a BERT model.  



### References:
Goswami, Dhiman, et al. Native Language Identification in Texts: A Survey. Vol. 1, 2024, pp. 3149–3160. Accessed 27 Apr. 2026.

Kramp, Sergey, et al. “BigNLI: Native Language Identification with Big Bird Embeddings.” ACL Anthology, May 2024, pp. 2375–2382, aclanthology.org/2024.lrec-main.212/. Accessed 28 Apr. 2026.

Kulmizev, Artur, et al. The Power of Character N-Grams in Native Language Identification. University of Groningen, 2017.

Perkins, Ria, and Tim Grant. “Native Language Influence Detection for Forensic Authorship Analysis: Identifying L1 Persian Bloggers.” The International Journal of Speech, Language and the Law, vol. 25, no. 1, 10 Sept. 2018, pp. 1–20, https://doi.org/10.1558/ijsll.30844. Accessed 26 Apr. 2026.

Tejas-Nanaware. “GitHub - Tejas-Nanaware/Native-Language-Identification: Identify the Native Language of an Author Using Neural Networks and BERT for Vector Representation.” GitHub, 2025, github.com/Tejas-Nanaware/Native-Language-Identification/tree/master. Accessed 27 Apr. 2026.

Nie, Yuzhe. “Native Language Identification from Text Using a Fine-Tuned GPT-2 Model.” PeerJ Computer Science, vol. 11, 28 May 2025, https://doi.org/10.7717/peerj-cs.2909. Accessed 27 Apr. 2026.

Stehwien, Sabrina, and Sebastian Padó. “Native Language Identification across Text Types: How Special Are Scientists?” Italian Journal of Computational Linguistics, vol. 2, no. 1, 1 June 2016, https://doi.org/10.4000/ijcol.348. Accessed 27 Apr. 2026.

Zhang, Wei, and Alexandre Salle. Native Language Identification with Large Language Models. 2023.






