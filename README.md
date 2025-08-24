# Applied Machine Learning

A collection of **hands-on case studies** applying classical ML techniques to real-world datasets.  
Each case study is self-contained with a notebook covering data exploration, preprocessing, modeling, and evaluation.

---

## 📚 Case Studies

1. **[Car Resale Price Prediction](case_studies/01_car_resale_price/)**  
   - **Goal**: Predict resale prices of used cars based on attributes like year, engine, fuel type, and seller details.  
   - **Techniques**: Data cleaning, exploratory analysis, feature engineering, and **linear regression** for price prediction.

2. **[Insurance Price Prediction](case_studies/02_insurance_price_prediction/)**
   - **Goal**: Predict insurance charges for individuals based on demographic and health factors.
   - **Techniques**: Exploratory analysis, categorical encoding, **linear regression** and evaluation via **MAE/MSE/R²**.

3. **[Credit Card Fraud Prediction](case_studies/03_credit_card_fraud/)**
   - **Goal**: Detect fraudulent credit card transactions in an imbalanced dataset.  
   - **Techniques**: Exploratory analysis, class imbalance handling, **Logistic Regression** and **K-Nearest Neighbors (KNN)**.
   
4. **[Insurance Claim Prediction (Porto Seguro Safe Driver)](case_studies/04_insurance_claim_prediction/)**  
   - **Goal**: Predict the probability that a driver will file an insurance claim in the future.  
   - **Techniques**: Extensive EDA on anonymized features, handling missing values, bivariate analysis for rare-but-important variables, encoding categorical features, feature selection, and **Logistic Regression / Random Forest** with evaluation via **ROC-AUC** and **F1-score** on imbalanced data.


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

