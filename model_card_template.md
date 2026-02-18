# Model Card

Model name: Census Classification Model

## Model Details
Model type: Supervised binary classification (Logistic Regression)

Intended use: Predict whether a person earns <=50K or >50K based on census features.

Version: 1.0

Authors / Maintainers: Richmond

Repository: https://github.com/datamillers/Deploying-a-Scalable-ML-Pipeline-with-FastAPI


## Intended Use
This model is intended for educational/demo purposes:
training a model from structured tabular data
preprocessing categorical + numeric features
saving/loading model artifacts
serving predictions via a FastAPI endpoint
Not intended for: hiring, lending, insurance decisions, or any real-world high-stakes use.

## Training Data
Training Data
Dataset: Census dataset provided in the project.
Target label: salary (binary: <=50K, >50K)
Features used: mixture of categorical and numerical features (e.g., workclass, education, marital-status, occupation, relationship, race, sex, native-country, etc.).

A train/test split is used during training (via the project’s training script and preprocessing pipeline).

## Evaluation Data
A held-out test split from the same dataset is used to evaluate performance after training.
## Metrics
The model is evaluated using classification metrics:
Precision
Recall
F1 score
(These are printed during training and also computed on categorical slices in slice_output.txt.)

Quantitative Analysis
From the training run output, the model achieved approximately:
Precision: ~0.73
Recall: ~0.56
F1: ~0.64
(These were printed during run, see screenshot log_regression for details under screenshot folder)
Exact numbers may vary slightly depending on split/random state and preprocessing.

## Ethical Considerations
This dataset includes sensitive demographic attributes. Using such features may introduce or amplify bias. Predictions could reflect historical inequities in the data.
This project is for learning and deployment practice only. If used in real applications, it would require:
Bias/fairness evaluation across groups
careful feature selection and governance
human oversight and transparency

## Caveats and Recommendations
The model may not generalize to populations outside the distribution of the training dataset.
Slice performance can vary greatly; please look over slice_output.txt for subgroup differences.
A convergence warning may occur during Logistic Regression training; consider increasing max_iter or scaling numeric features if improving training stability is required.
For improved performance, consider experimenting with alternative models (e.g., Random Forests, Decision Trees) and hyperparameter tuning.

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf