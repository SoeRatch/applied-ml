# Applied Machine Learning

A collection of **hands-on case studies** applying classical ML techniques to real-world datasets.  
Each case study is self-contained with a notebook covering data exploration, preprocessing, modeling, and evaluation.

---

## 📚 Case Studies

1. **[Car Resale Price Prediction](01_car_resale_price/)**  
   - **Goal**: Predict resale prices of used cars based on attributes like year, engine, fuel type, and seller details.  
   - **Techniques**: Data cleaning, exploratory analysis, feature engineering, and **linear regression** for price prediction.

2. **[Insurance Price Prediction](02_insurance_price_prediction/)**
   - **Goal**: Predict insurance charges for individuals based on demographic and health factors.
   - **Techniques**: Exploratory analysis, categorical encoding, **linear regression** and evaluation via **MAE/MSE/R²**.

3. **[Credit Card Fraud Prediction](03_credit_card_fraud/)**
   - **Goal**: Detect fraudulent credit card transactions in an imbalanced dataset.  
   - **Techniques**: Exploratory analysis, class imbalance handling, **Logistic Regression** and **K-Nearest Neighbors (KNN)**.
   
4. **[Insurance Claim Prediction (Porto Seguro Safe Driver)](04_insurance_claim_prediction/)**  
   - **Goal**: Predict the probability that a driver will file an insurance claim in the future.  
   - **Techniques**: Extensive EDA on anonymized features, handling missing values, bivariate analysis for rare-but-important variables, encoding categorical features, feature selection, and **Logistic Regression / Random Forest** with evaluation via **ROC-AUC** and **F1-score** on imbalanced data.

5. **[Loan Approval Prediction](05_loan_approval_prediction/)**  
   - **Goal**: Predict loan approval based on applicant attributes such as income, loan amount, credit history, and property area.  
   - **Techniques**: Preprocessing, **Decision Tree**, **Random Forest**, **AdaBoost**, **Gradient Boosting**, **XGBoost**.  
   - **Evaluation**: Accuracy, precision, recall, F1-score (~78% with ensembles).
   
6. **[Heart Failure Prediction](06_heart_failure_prediction/)**  
   - **Goal**: Predict the likelihood of heart disease in patients based on clinical and demographic features.  
   - **Techniques**: EDA, categorical encoding, preprocessing, and training multiple classifiers including **Logistic Regression, Random Forest, Gradient Boosting, XGBoost, SVM, Naive Bayes, KNN**.  
   - **Evaluation**: Cross-validation accuracy, test accuracy, F1-score (~90% with ensembles, Random Forest performed best).  



*(More case studies will be added over time.)*

---

## Quick Start

```bash
git clone https://github.com/SoeRatch/applied-ml.git
cd applied-ml

# Navigate to specific case folder, then:
# pip install -r case_studies/<folder_name>/requirements.txt

# launch notebooks via Jupyter or VS Code
```

