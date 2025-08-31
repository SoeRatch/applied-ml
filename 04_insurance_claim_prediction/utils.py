# utils.py
import pandas as pd
import scipy.stats as stats
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def categorical_feature_analysis(df, cat_cols, target_col='target', drop_threshold=0.3, p_value_threshold=0.05):
    """
    Analyze categorical features against target using Chi-square test and Cramér's V.
    
    Parameters:
        df (pd.DataFrame): Dataset containing features and target.
        cat_cols (list): List of categorical columns to analyze.
        target_col (str): Name of the target column.
        drop_threshold (float): Cramér's V threshold below which feature is flagged for drop.
        p_value_threshold (float): p-value threshold to consider association significant.
        
    Returns:
        pd.DataFrame: Summary with p-value, Cramér's V, and drop suggestion.
    """
    results = []

    for col in cat_cols:
        # Crosstab of feature vs target
        ct = pd.crosstab(df[col], df[target_col])

        # Chi-square test
        chi2, p, dof, ex = stats.chi2_contingency(ct)

        # Cramér's V calculation
        n = ct.sum().sum()
        cramers_v = np.sqrt(chi2 / (n * (min(ct.shape)-1)))

        # Suggest drop if association is not significant or Cramér's V is below threshold
        drop_flag = (p >= p_value_threshold) or (cramers_v < drop_threshold)

        results.append({
            'Feature': col,
            'Chi2_p_value': round(p, 6),
            'Cramers_V': round(cramers_v, 4),
            'Drop': drop_flag
        })

    return pd.DataFrame(results).sort_values(by='Cramers_V', ascending=False)


# Define a function to train and evaluate the model
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    """
    Train a given model and evaluate it using standard classification metrics.

    Parameters:
        model : sklearn-like estimator
            Any classifier with .fit() and .predict() methods
        X_train, y_train : training features and labels
        X_test, y_test : testing features and labels

    Returns:
        dict : evaluation metrics (precision, recall, f1, roc_auc)
    """
    # Train the model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Calculate metrics
    metrics = {
        'accuracy': f"{accuracy_score(y_test, y_pred)*100:.2f}%",
        'precision': f"{precision_score(y_test, y_pred, zero_division=0)*100:.2f}%",
        'recall': f"{recall_score(y_test, y_pred, zero_division=0)*100:.2f}%",
        'f1': f"{f1_score(y_test, y_pred, zero_division=0)*100:.2f}%",
        'roc_auc': f"{roc_auc_score(y_test, y_pred)*100:.2f}%"
    }


    return metrics