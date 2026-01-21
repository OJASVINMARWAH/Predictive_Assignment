Credit Card Fraud Detection using Sampling Techniques

This project explores the impact of different sampling methods on machine learning models when working with an imbalanced credit card transaction dataset.

## Discussion
In this experiment, the main goal was to understand how different sampling techniques help machine learning models deal with a highly imbalanced credit card fraud dataset.

Initially, the dataset contained far more legitimate transactions than fraudulent ones, which made it difficult for models to correctly learn the fraud patterns. To overcome this, five different sampling strategies were applied, and each balanced version of the dataset was tested on five machine learning models.

From the results, it became very clear that sampling plays a critical role in model performance.

Random Forest consistently performed the best among all models. In fact, when combined with hybrid sampling methods like SMOTEENN and SMOTETomek, it achieved 100% accuracy, showing that ensemble models benefit greatly from a well-balanced and clean dataset.

Logistic Regression and Decision Tree also performed strongly after resampling, especially with SMOTE-based techniques. On the other hand, Naive Bayes and SVM were more sensitive to the data distribution and their performance dropped significantly when simple under-sampling was used, mainly due to loss of important information.
Overall, the experiment proves that:

Imbalanced data can seriously affect prediction quality.

Hybrid sampling methods are more reliable than using only over-sampling or under-sampling.

Random Forest is the most robust and accurate model for this type of problem.
