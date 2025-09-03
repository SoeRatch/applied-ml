# Heart Disease Prediction Case Study

## Objective
The goal of this project is to **predict the likelihood of heart disease** in patients based on clinical and demographic features.  
This is a **binary classification problem**, where the target variable `HeartDisease` indicates whether the patient has heart disease (`1`) or not (`0`).  
Accurate prediction can assist healthcare professionals in **early detection** and **timely intervention** for high-risk patients.

---

## Dataset Overview
The dataset contains patient information including demographics, clinical measurements, and test results.

**Features:**
- `Age`: Age of the patient (years)  
- `Sex`: Sex of the patient (M/F)  
- `ChestPainType`: Chest pain type (TA, ATA, NAP, ASY)  
- `RestingBP`: Resting blood pressure (mm Hg)  
- `Cholesterol`: Serum cholesterol (mg/dl)  
- `FastingBS`: Fasting blood sugar (`1` if >120 mg/dl, else `0`)  
- `RestingECG`: Resting ECG results (Normal, ST, LVH)  
- `MaxHR`: Maximum heart rate achieved  
- `ExerciseAngina`: Exercise-induced angina (Y/N)  
- `Oldpeak`: ST depression induced by exercise  
- `ST_Slope`: Slope of the peak exercise ST segment (Up, Flat, Down)  
- `HeartDisease`: Target variable (`1`: heart disease, `0`: normal)  

---

## Exploratory Data Analysis (EDA)
- **Key correlations:**  
  - `Oldpeak` (ST depression) **positively correlated** with heart disease.  
  - `MaxHR` (maximum heart rate) **negatively correlated** with heart disease.  
  - `Age` and `FastingBS` also show moderate positive correlation.  
- **Outliers detected:**  
  - `RestingBP` and `Cholesterol` contain zero values (likely data issues).  
- **Class balance:**  
  - Dataset is **fairly balanced** between positive and negative cases.  

---

## Preprocessing
- **Categorical Encoding:** Used **one-hot encoding** for categorical variables.  
- **Splitting:** Train-test split with stratification (`80-20`).  
- **Scaling:** Not applied (tree-based models handle scaling automatically).  

---

## Models Trained
The following machine learning models were evaluated:
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- Random Forest  
- AdaBoost  
- Gradient Boosting  
- XGBoost  
- Support Vector Machine (SVM)  
- Gaussian Naive Bayes  

Evaluation metrics included **cross-validation accuracy, test accuracy, and F1-score**.

---

## Results
| Model                   | CV Accuracy | Test Accuracy | F1 Score |
|--------------------------|-------------|---------------|----------|
| Random Forest            | **0.85**    | **0.89**      | **0.903** |
| Gradient Boosting        | 0.85        | 0.89          | 0.902    |
| Logistic Regression      | 0.85        | 0.88          | 0.900    |
| Naive Bayes              | 0.85        | 0.88          | 0.898    |
| AdaBoost                 | 0.85        | 0.88          | 0.897    |
| XGBoost                  | 0.84        | 0.87          | 0.887    |
| Decision Tree            | 0.81        | 0.79          | 0.814    |
| SVM                      | 0.72        | 0.71          | 0.743    |
| KNN                      | 0.71        | 0.69          | 0.726    |

---

## Conclusion & Recommendation
- **Best Model:** **Random Forest** achieved the highest F1-score (~0.903), closely followed by Gradient Boosting and Logistic Regression.  
- **Key Predictors:** `Oldpeak`, `MaxHR`, `Age`, and `FastingBS`.  
- **Recommendation:**  
  - Use **Random Forest** as the final model due to its robustness and strong performance.  
  - Perform **hyperparameter tuning** for further improvement.  
  - Address **outliers** (e.g., RestingBP = 0, Cholesterol = 0).  
  - Validate performance on an **external dataset** before deployment.  

Note that this model should be used as a **decision-support tool**, not a standalone diagnostic system.

