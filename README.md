## Predicting_Protien_Thermostability
I will be using this repository while learning data preparation - EDA and Feature extraction.
Dataset is copied from the kaggle competition - Novozymes Enzyme Stability Prediction.

This notebook was a 'get messy real fast' trial to participate in the competition - https://www.kaggle.com/code/rzachariah/gemme-catboost?scriptVersionId=115345757.

I am now working through the posts and notebooks shared by various participants as I apply 'Design Thinking' principles to explore the data, make sense of it, and extract features of interest.

## Background information
Enzymes are proteins that act as catalysts in the chemical reactions of living organisms. The goal is to predict the thermostability of enzyme variants. The experimentally measured thermostability (melting temperature) data includes natural sequences, as well as engineered sequences with single or multiple mutations upon the natural sequences.

Understanding and accurately predict protein stability is a fundamental problem in biotechnology. Its applications include enzyme engineering for addressing the world’s challenges in sustainability, carbon neutrality and more. Improvements to enzyme stability could lower costs and increase the speed scientists can iterate on concepts.

Computational protein stability prediction based on physics principles have made remarkable progress thanks to advanced physics-based methods such as FoldX, Rosetta, and others. Recently, many machine learning methods were proposed to predict the stability impact of mutations on protein based on the pattern of variation in natural sequences and their three dimensional structures. More and more protein structures are being solved thanks to the recent breakthrough of AlphaFold2. 

However, accurate prediction of protein thermal stability remains a great challenge.

The goal is to develop a model to predict/rank the thermostability of enzyme variants based on experimental melting temperature data.
