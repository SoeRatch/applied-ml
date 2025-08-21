# Car Resale Price Prediction

Predicting the **resale price of cars** using Linear Regression.  
This notebook covers end-to-end exploration, core linear-regression assumptions, OLS diagnostics, and a **from-scratch implementation of Gradient Descent** (univariate).

---

## Dataset

Loaded from `../data/CarPred.csv` with columns such as:

- `selling_price` (target, in lakhs)  
- `year` (manufacturing year)  
- `km_driven`  
- `engine` (cc)  
- `max_power`  
- `make`, `model`  
- `transmission_type` (0 = manual, 1 = automatic)  
- `seats_cop`, `seats_family`, `seats_large` (binary indicators)  
- Fuel indicators: `fuel_cng`, `fuel_diesel`, `fuel_electric`, `fuel_lpg`, `fuel_patrol`  
- Seller indicators: `seller_dealer`, `seller_self`

> **Problem type:** Supervised learning  
> **Objective type:** Regression (predict a continuous value — `selling_price`)

---

## Workflow

### 1) Initial EDA (Univariate Focus)
- Scatter plot of **`max_power` vs `selling_price`** to motivate a linear relationship.
- For simplicity, the predictive modeling starts with a **single feature** (`max_power`) to build intuition with **Simple Linear Regression**.

### 2) Linear Regression Assumptions (with Diagnostics)
Using **statsmodels OLS** on a multivariate set of predictors:

['year','km_driven','engine','max_power','transmission_type',
'seats_cop','seats_family','seats_large','fuel_cng','fuel_diesel',
'fuel_electric','fuel_patrol','fuel_lpg','seller_dealer','seller_self']


Assumptions and checks performed:
- **Linearity** — Actual vs Predicted scatter with 45° reference line.  
- **Homoscedasticity** — Residuals vs Predicted plot with y=0 guide.  
- **Normality of Errors** — Histogram of residuals.  
- **No Autocorrelation** — **Durbin–Watson** statistic (≈2 indicates no autocorrelation).  
- **No Perfect Multicollinearity** — **VIF** computed per feature.

> These diagnostics help validate whether a linear model is appropriate and guide feature handling.

### 3) Linear Regression Refresher (Theory)
- Hypothesis: **\( y = theta_0 + theta_1 * x \)**  
- Cost Function: **Mean Squared Error (MSE)**  
- Feedback loop & Gradient Descent intuition.

### 4) Gradient Descent — Intuition & Visualization
- Convex function toy example **\( y = (x - 5)^2 \)** to visualize descent.
- Effect of **learning rate** on convergence (overshooting vs smooth approach).
- **Early stopping** discussion (fixed iterations, convergence threshold, validation-based stopping).

### 5) From-Scratch Training (Univariate Model)
- **Feature**: `max_power` (standardized: subtract mean, divide by std).  
- Implemented functions:
  - `hypothesis(x, theta)`  
  - `gradient(X, Y, theta)`  
  - `error(X, Y, theta)`  
  - `gradient_descent(X, Y, max_steps=..., learning_rate=...)`
- Example run: `max_steps=50`, learning rate `0.1`, yielding parameters like:  
  - **θ₀ ≈ 264,899.50**, **θ₁ ≈ 63,179.88** *(with standardized `max_power`; values may vary)*

### 6) Visualizations
- **Error vs Iteration** (training loss curve).  
- **θ₀ and θ₁ trajectories** across iterations.  
- **Data + fitted line** (scatter of standardized `max_power` vs `selling_price` with prediction line).

---

## Learnings
- How to validate linear model assumptions (linearity, homoscedasticity, normality, autocorrelation, multicollinearity).  
- How **Gradient Descent** works, why **feature scaling** matters, and how **learning rate** affects convergence.  
- Building a **Simple Linear Regression** model from scratch and interpreting results responsibly.

---

## Tech Stack
- **Python**, **NumPy**, **Pandas**  
- **Matplotlib** (and a small use of **Seaborn** for styling)  
- **statsmodels** (OLS, Durbin–Watson), VIF via `statsmodels.stats.outliers_influence`

---

## Files
- `car_resale_price_prediction.ipynb` - Jupyter Notebook with full workflow and analysis.  

## How to Run
```bash
jupyter notebook car_resale_price_prediction.ipynb
```


