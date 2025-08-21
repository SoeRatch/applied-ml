# Insurance Price Prediction

This case study focuses on building a regression model to predict **insurance charges** based on customer demographic and health-related features.  

## Dataset
The dataset contains the following features:
- **age**: Age of the individual  
- **sex**: Gender (male/female)  
- **bmi**: Body Mass Index  
- **children**: Number of dependents  
- **smoker**: Smoking status (yes/no)  
- **region**: Residential area (northeast, southeast, southwest, northwest)  
- **charges**: Insurance cost (target variable)  

## Approach
1. **Data Exploration & Cleaning**  
   - Checked distributions of numerical and categorical features.  
   - Handled categorical variables with encoding.  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized the effect of **smoking**, **age**, and **BMI** on charges.  
   - Compared charges across different regions.  

3. **Feature Engineering**  
   - Converted categorical variables (`sex`, `smoker`, `region`) into numerical form using encoding techniques.  

4. **Modeling**  
   - Built a **Linear Regression model** to predict insurance charges.  
   - Evaluated model performance with metrics like **R² score** and **Mean Squared Error (MSE)**.  

## Key Insights
- **Smokers** pay significantly higher charges compared to non-smokers.  
- **Age** and **BMI** are strong predictors of insurance cost.  
- Linear regression provides a baseline, but more advanced models could improve performance.  

## Files
- `insurance_price_prediction.ipynb` - Jupyter Notebook with full workflow and analysis.  

## How to Run
```bash
jupyter notebook insurance_price_prediction.ipynb
```
