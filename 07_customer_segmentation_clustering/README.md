# Customer Segmentation Case Study

## Objective
The goal of this project is to **segment mall customers into distinct groups** using clustering techniques.  
The segmentation is based on **demographic features (age, gender, income)** and **spending behavior**.  
These insights can help businesses with **targeted marketing, personalized promotions, and improved customer engagement**.

---

## Dataset Overview
The dataset used is the **Mall Customers dataset**, containing customer demographics and spending scores.

**Features:**
- `CustomerID`: Unique identifier for each customer (removed during preprocessing)  
- `Gender`: Gender of the customer (Male/Female)  
- `Age`: Age of the customer (years)  
- `Annual Income (k$)`: Annual income of the customer (in thousands)  
- `Spending Score (1–100)`: Score assigned by the mall based on customer behavior and spending  

---

## Exploratory Data Analysis (EDA)
- **Age vs Spending Score:** Younger customers generally have higher spending scores (negative correlation with age).  
- **Annual Income vs Spending Score:** Clear clusters are visible, indicating potential customer segments.  
- **Gender-based trends:** Female customers show slightly higher spending on average.  
- **Distributions:**  
  - Many customers are in their early 30s.  
  - Annual income distribution is uneven.  
  - Spending score varies widely, enabling meaningful clustering.  

---

## Preprocessing
- **Categorical Encoding:** Converted `Gender` to numerical values using one-hot encoding.  
- **Scaling:** Applied `StandardScaler` to normalize numerical features for clustering.  

---

## Clustering Techniques Applied
- **K-Means Clustering:**
  - Optimal `k` tested using Elbow Method, Silhouette Score, and Davies-Bouldin Score.  
  - For `k=5`, silhouette score = **0.27**, Davies-Bouldin score = **1.84**.  

- **Agglomerative Hierarchical Clustering:**  
  - Dendrogram analysis suggested **5 clusters**.  
  - Outperformed K-Means with higher silhouette score and lower Davies-Bouldin score.  

- **DBSCAN:**  
  - Tested with varying epsilon values.  
  - Did not perform well due to limited dataset size and few outliers.  

---

## Results
- **Best Method:** Agglomerative Hierarchical Clustering  
- **Final Customer Segments (5 Clusters):**
  1. High Income & Lavish Lifestyle  
  2. Average Income & Average Lifestyle  
  3. High Income & Meagre Lifestyle  
  4. Low Income & Meagre Lifestyle  
  5. Low Income & Lavish Lifestyle  

---

## Conclusion
- **Agglomerative Clustering** provided the most meaningful and stable segmentation.  
- Clear customer segments were identified, reflecting differences in **income levels** and **spending behavior**.  
- These segments can directly help businesses create **personalized marketing strategies** and **targeted offers**.  
- While K-Means showed reasonable results, Agglomerative performed better on both **Silhouette** and **Davies-Bouldin** scores.  

---

This contains the notebook for the case study.

