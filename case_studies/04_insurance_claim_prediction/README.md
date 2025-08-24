# Insurance Claim Prediction (Porto Seguro Case Study)

This case study explores the **Porto Seguro Safe Driver Prediction** dataset (Kaggle competition). The goal is to predict whether a driver will file an insurance claim within the next year. The dataset is **highly imbalanced**, requiring careful preprocessing, resampling, and evaluation.

---

## Objective
- Predict whether a driver will file an insurance claim (`target = 1`).  
- Handle **class imbalance** effectively to improve minority class detection.  
- Compare the impact of different **resampling techniques** on model performance.  

---

## Dataset Overview
- **Rows**: ~595,000  
- **Features**: 59 anonymized (binary, categorical, continuous)  
- **Target**: Binary (0 = no claim, 1 = claim)  
- **Imbalance**: Only **3.64%** of policyholders filed claims  

Missing values are encoded as `-1` instead of `NaN`.  

---

##  EDA Highlights

1. **Target Imbalance**  
   - 96.35% = no claim, 3.64% = claim, imbalance ratio ≈ 27:1.  

2. **Missing Values**  
   - `ps_car_03_cat` (~69%) and `ps_car_05_cat` (~45%) had high missingness.  
   - Despite this, **bivariate analysis showed strong association with the target**, so they were imputed and kept.  

3. **Binary Features**  
   - Some (`ps_ind_10_bin`, `ps_ind_11_bin`, `ps_ind_13_bin`) were almost constant indicating low variance.  
   - Others (`ps_ind_07_bin`, `ps_ind_17_bin`) showed meaningful separation between claim vs no-claim.  

4. **Categorical Features**  
   - Claim rates varied significantly across categories (e.g., certain `ps_car_XX_cat` values).  
   - `ps_car_10_cat` and `ps_ind_02_cat` showed weak/no predictive power and were dropped.  

5. **Numeric Features**  
   - Features like `ps_reg_03`, `ps_car_13` showed noticeable shifts between claim/no-claim groups.  
   - Many were skewed - standardized for models like KNN.  

6. **Correlation Analysis**  
   - Most features were weakly correlated, suggesting low redundancy.  

---

## Preprocessing
- **Dropped low-value features**: e.g., low-variance binaries and weak categorical predictors.  
- **Imputation**:  
  - Numeric - median replacement for `ps_reg_03`, `ps_car_14`.  
  - Categorical - mode replacement for missing categories (including `ps_car_03_cat` and `ps_car_05_cat`).  
- **Scaling**: StandardScaler applied to numeric features (important for KNN).  
- **Encoding**: One-hot encoding for categorical features.  

---

## Handling Class Imbalance
Five resampling techniques were applied:  
- **Random Under-sampling**  
- **Random Over-sampling**  
- **SMOTE** (synthetic oversampling)  
- **Tomek Links** (undersampling, boundary cleaning)  
- **SMOTE-Tomek** (combination approach)  

---

## Models Trained
- **Logistic Regression** (baseline linear model)  
- **KNN (k=5)** (non-linear, distance-based model)  

Both models were trained & evaluated on each resampled dataset.  

---

## Results (Key Findings)

- **Without resampling**:  
  - High accuracy (~96%) but **F1 = 0%** - models ignored minority class.  

- **Logistic Regression**  
  - Best with **SMOTE / SMOTE-Tomek** - Accuracy ~96.9%, Precision ~99%, Recall ~94.6%, F1 ~96.8%.  
  - Balanced performance, strong detection of minority class.  

- **KNN**  
  - With **Over-sampling** - Recall reached **100%**, but Precision dropped (~90%), leading to lower F1 (~94.7%).  
  - With **SMOTE / SMOTE-Tomek** - Very high recall but poor precision, resulting in moderate F1 (~77%).  

- **Under-sampling** consistently underperformed due to information loss.  
- **Tomek Links** cleaned data but led to models failing to capture the minority class.  

---

## Conclusion
- **Resampling is essential**: Without it, models collapse to predicting only the majority class.  
- **SMOTE / SMOTE-Tomek with Logistic Regression** gave the **best trade-off** across precision, recall, and F1.  
- **KNN** captured all positives (recall = 100%) under oversampling but at the cost of precision - not ideal for high-stakes insurance risk prediction.  
- This demonstrates the importance of **balancing recall (catching claims) with precision (avoiding false alarms)** depending on business needs.  
