# Credit Card Fraud Detection

## Objective
The goal of this case study is to detect fraudulent credit card transactions using **Logistic Regression** and **K-Nearest Neighbors (KNN)**.  
Since the dataset is highly imbalanced, we apply various resampling techniques to handle class imbalance and improve performance.

---

## Dataset Overview
- **V1 – V28**: Anonymized PCA-based features.  
- **Time**: Seconds elapsed since the first transaction.  
- **Amount**: Transaction value.  
- **Class**: Target variable (0 = legitimate, 1 = fraud).  

The dataset is **severely imbalanced**: legitimate transactions greatly outnumber fraud cases.

---

## Preprocessing
1. **Feature Scaling** – Standardized all features (mean = 0, std = 1) to improve KNN performance.  
2. **Train-Test Split** – 80% training, 20% testing with stratification to preserve class ratio.  

---

## Handling Class Imbalance
We applied the following resampling techniques:  
- **Random Under Sampling (RUS):** Removes majority class samples.  
- **Random Over Sampling (ROS):** Duplicates minority samples.  
- **SMOTE:** Creates synthetic minority samples.  
- **Tomek Links:** Removes borderline majority samples.  
- **SMOTE-Tomek:** Combines SMOTE with Tomek Links.  

---

## Evaluation Metrics
- **Precision:** Correctness of fraud predictions (low false positives).  
- **Recall:** Ability to detect fraud cases (low false negatives).  
- **F1 Score:** Balance between precision and recall.  
- **ROC AUC:** Ability to rank fraud vs non-fraud cases.  

---

## Results Interpretation – Logistic Regression
- **RUS/ROS/SMOTE/SMOTE-Tomek:** Very high recall but far too many false positives.  
- **Tomek Links:** Lower recall but much higher precision and balance.  

✅ Best trade-off: **Tomek Links**  
- Use ROS/SMOTE when catching every fraud is critical (manual review possible).  
- Use Tomek Links when false positives are costly (e.g., automatic blocking).  

---

## Results Interpretation – KNN
- **RUS:** Very high recall but unusably low precision.  
- **ROS/SMOTE/SMOTE-Tomek:** Good recall with some precision, but still many false positives.  
- **Tomek Links:** Highest precision and strong balance, fewer false alarms.  

✅ Best trade-off: **Tomek Links**  
- Use ROS/SMOTE for maximum fraud detection.  
- Use Tomek Links when reducing false positives is the priority.  

---

## Conclusion
We tackled class imbalance with **RUS, ROS, SMOTE, Tomek Links, and SMOTE-Tomek** and applied **Logistic Regression** and **KNN** to detect fraudulent transactions.  
Overall, **Tomek Links consistently provided the most balanced results**, while oversampling methods (ROS/SMOTE) ensured maximum fraud detection at the expense of false alarms.


## Files
- `credit_card_fraud_prediction.ipynb` - Jupyter Notebook with full workflow and analysis.  

## How to Run
```bash
jupyter notebook credit_card_fraud_prediction.ipynb
```
