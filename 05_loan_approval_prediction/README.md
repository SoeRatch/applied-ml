# Loan Approval Prediction Case Study

## Objective
The goal of this case study is to predict whether a loan application will be approved based on various applicant attributes. The dataset includes information such as income, loan amount, credit history, and more. The target variable is `Loan_Status`, a binary classification indicating whether the loan was approved (`Y`) or not (`N`).

---

## Dataset Overview
The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| Loan_ID | Unique loan identifier |
| Gender | Male/Female |
| Married | Applicant married (Yes/No) |
| Dependents | Number of dependents |
| Education | Applicant education (Graduate/Not Graduate) |
| Self_Employed | Self-employed (Yes/No) |
| ApplicantIncome | Applicant's income |
| CoapplicantIncome | Coapplicant's income |
| LoanAmount | Loan amount in thousands |
| Loan_Amount_Term | Term of loan in months |
| Credit_History | Credit history meets guidelines (1/0) |
| Property_Area | Urban/Semi-Urban/Rural |
| Loan_Status | Target variable: Loan approved (Y/N) |

---

## Preprocessing Steps
1. **Missing Value Handling**
   - Categorical features: Imputed using mode.
   - Numerical features: Imputed using median (LoanAmount) or mode (Loan_Amount_Term, Credit_History).
   - `Dependents`: Replaced `3+` with 3 and converted to numeric.
2. **Encoding Categorical Variables**
   - Label encoding for categorical columns: `Gender`, `Married`, `Education`, `Self_Employed`, `Property_Area`.
   - Target variable `Loan_Status` encoded as 0 (N) and 1 (Y).
3. **Train-Test Split**
   - Split the dataset into training and testing sets with a 70-30 ratio.

---

## Models Used
1. **Decision Tree**
   - Trained with `entropy` and `gini` criteria.
   - Pre-pruning applied using `max_depth` and `min_samples_split`.
   - Hyperparameter tuning with `GridSearchCV`.

2. **Bagging (Random Forest)**
   - Trained with 100 estimators and bootstrap sampling.
   - Hyperparameter tuning with `GridSearchCV` for `n_estimators`, `max_depth`, and `min_samples_split`.

3. **Boosting**
   - **AdaBoost**: Base estimator is Decision Tree; hyperparameters tuned using `GridSearchCV`.
   - **Gradient Boosting**: Trained with `GradientBoostingClassifier`; hyperparameter tuning applied.
   - **XGBoost**: Trained using `XGBClassifier`; hyperparameter tuning applied.

---

## Evaluation Metrics
- **Accuracy**: Overall correctness of predictions.
- **Confusion Matrix**: Counts of True Positive, True Negative, False Positive, False Negative.
- **Precision, Recall, F1-Score**: Per-class evaluation metrics to assess model performance, especially on imbalanced classes.

---

## Key Insights
- Decision Trees are simple and interpretable but prone to overfitting.
- Random Forest and boosting methods significantly improve performance by reducing variance or focusing on hard-to-predict instances.
- On this dataset, Random Forest, AdaBoost, Gradient Boosting, and tuned XGBoost all achieved similar accuracy (~78%).
- Feature importance from Random Forest indicates `Credit_History` and `ApplicantIncome` are strong predictors.

---

## Results Summary

| Model | Accuracy |
|-------|---------|
| Decision Tree (Entropy) | 71.35% |
| Decision Tree (Gini) | 64.32% |
| Decision Tree (Pre-Pruning) | 74.05% |
| Best Decision Tree (Grid Search) | 77.83% |
| Random Forest | 77.83% |
| Random Forest (Grid Search) | 78.38% |
| AdaBoost | 77.83% |
| AdaBoost (Grid Search) | 78.38% |
| Gradient Boosting | 75.68% |
| Gradient Boosting (Grid Search) | 77.83% |
| XGBoost | 74.59% |
| XGBoost (Grid Search) | 77.83% |

---

## Conclusion
- Ensemble methods outperform standalone Decision Trees on this dataset.
- Random Forest and boosting techniques (AdaBoost, Gradient Boosting, XGBoost) all achieve similar performance after hyperparameter tuning.
- Random Forest is recommended for a robust, easy-to-tune model.
- Boosting methods are suitable when fine-tuning and computational resources are available.
