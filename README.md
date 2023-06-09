# Mental Health Alerts for K-12: Reverse Engineering GoGuardian Beacon
## Problem
There is a need for mental health resources in K-12 education but school staff are often overwhelmed with cases. In this project, we reverse engineer an application called GoGuardian Beacon that notifies designated faculty and guardians about online activity that indicates risk of harm to self or others. We decided to implement the model that GoGuardian uses for classification. The model determines whether a student is at risk of harming themselves or others through classification (supervised learning)


## Files 
### data_collection.ipynb 
Samples and cleans data from various sources to be used to train and test our models

### ml_classification.ipynb 
Pre-processes data for machine learning models and then trains and tests three machine learning models: SVM, LogisticRegression, and Multinomial Naive Bayes.

### neural_networks.ipynb
Pre-processes data for neural networks and then trains and tests three neural networks: LSTM Layers, Bidirectional Layers, and 1-D Convolutional Networks

