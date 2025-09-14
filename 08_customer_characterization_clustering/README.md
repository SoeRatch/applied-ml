# Customer Characterization Case Study

## Objective

The objective of this case study is to **characterize customers in a marketing campaign dataset** by identifying meaningful clusters based on **income, spending habits,purchasing behavior and campaign responses**.  
The analysis uses **K-Means, Hierarchical, and DBSCAN clustering** to uncover hidden customer patterns that can guide **targeted marketing strategies, improve engagement, and optimize business decisions**.

---

## Dataset Overview
The dataset used is the **Marketing Campaign dataset**, containing demographic, lifestyle, and purchasing information along with responses to past campaigns.

#### Initial Dataset Features (raw data provided)

- **ID:** Unique identifier assigned to each customer.  
- **Year_Birth:** Year of birth of the customer.  
- **Education:** Level of education of the customer.  
- **Marital_Status:** Marital status of the customer.  
- **Income:** Annual household income of the customer.  
- **Kidhome:** Number of small children in the household.  
- **Teenhome:** Number of teenagers in the household.  
- **Dt_Customer:** Date when the customer enrolled with the company.  
- **Recency:** Number of days since the customer’s last purchase.  
- **MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds:** Amount spent by the customer on different product categories in the last two years.  
- **NumDealsPurchases:** Number of purchases made using a discount.  
- **NumWebPurchases:** Number of purchases made through the company’s website.  
- **NumCatalogPurchases:** Number of purchases made using a catalog.  
- **NumStorePurchases:** Number of purchases made directly in stores.  
- **NumWebVisitsMonth:** Number of visits to the company’s website in the last month.  
- **AcceptedCmp1 – AcceptedCmp5:** Whether the customer accepted offers in previous marketing campaigns.  
- **Response:** Whether the customer accepted the offer in the last marketing campaign.  
- **Complain:** Whether the customer has complained in the last 2 years.  
- **Z_CostContact:** Constant cost associated with each marketing contact.  
- **Z_Revenue:** Constant revenue associated with each sale.  

#### Final Features Used for Clustering (after preprocessing & feature engineering)
- **Education:** Standardized education level of the customer.  
- **Marital_Status:** Simplified into broader categories (Partner / Single).  
- **Kids:** Total number of children in the household (`Kidhome` + `Teenhome`).  
- **Income:** Cleaned and imputed annual household income.  
- **Recency:** Days since the customer’s last purchase.  
- **Expenses:** Total spending across all product categories.  
- **Purchases:** Total purchases across all channels (store, web, catalog, deals).  
- **TotalAcceptedCmp:** Total number of campaigns accepted by the customer.  
- **Complain:** Whether the customer has complained in the last 2 years.  
- **Response:** Whether the customer accepted the offer in the last campaign.  
- **Days_as_client:** Number of days since customer enrollment (`latest_date - Dt_Customer`).

This cleaned and engineered feature set was then used for clustering (KMeans, DBSCAN, Hierarchical) and customer characterization.

---

## Exploratory Data Analysis (EDA)
- **Income distribution:** Presence of outliers with a right-skewed distribution.  
- **Expenses and Purchases:** Strong variability across customers, suggesting potential cluster separation.  
- **Correlation analysis:** Purchases and Expenses are positively correlated, indicating similar behavioral traits.  
- **Categorical simplification:** Education and Marital Status consolidated into broader, interpretable categories.  

---

## Preprocessing
- **Missing values:** Median imputation for `Income`.  
- **Feature engineering:**  
  - Combined spending (`Expenses`) and purchases (`Purchases`) into aggregate measures.  
  - Created `Kids`, `TotalAcceptedCmp`, and `Days_as_client`.  
- **Encoding:**  
  - Ordinal encoding for `Education` (Undergraduate < Graduate < Postgraduate).  
  - Label encoding for `Marital_Status`.  
- **Outlier removal:** IQR method applied to numeric columns.  
- **Scaling:** Standardized features with `StandardScaler` for clustering.  

---

## Clustering Techniques Applied
- **K-Means Clustering:**
  - Optimal clusters tested with Elbow Method and Silhouette Scores.  
  - Fine-tuned with different `n_clusters`, initialization methods, and iterations.  
  - Achieved balanced performance and interpretable groups.  

- **Agglomerative Hierarchical Clustering:**  
  - Linkage methods (`ward`, `complete`, `average`) explored.  
  - Able to capture diverse customer behaviors.  

- **DBSCAN:**  
  - Fine-tuned across multiple `eps` and `min_samples`.  
  - Good at detecting outliers but struggled to separate meaningful customer groups.  

---

## Cluster Evaluation
- **Metrics Used:** Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Score.  
- **Results:**  
  - **K-Means:** Best overall balance of separation and compactness.  
  - **Hierarchical:** Moderate but acceptable performance, useful for uncovering diverse patterns.  
  - **DBSCAN:** Identified outliers effectively but performed poorly in forming clusters.  

---

## Cluster Characterization
- **K-Means Tuned:** Groups differentiated by **income, expenses, and purchase frequency**.  
- **Hierarchical Tuned:** Revealed diverse customer behaviors across spending and engagement levels.  
- **DBSCAN Tuned:** Labeled most customers as noise, highlighting its strength in **outlier detection**.  

---

## Validation
- **PERMANOVA tests:** Confirmed significant differences in **Income, Expenses, and Purchases** across K-Means clusters.  
- Clusters were statistically meaningful, not just random partitions.  

---

## Conclusion
- **K-Means clustering** provided the most balanced and interpretable results, supported by strong validation metrics and PERMANOVA tests.  
- **Hierarchical clustering** also uncovered meaningful behavioral differences, making it a suitable alternative.  
- **DBSCAN**, while useful for spotting outliers, was not effective for segmentation in this dataset.  

**Overall, K-Means or Hierarchical clustering are recommended approaches for actionable customer characterization in marketing.**

---

This repository contains the notebook for the case study.
