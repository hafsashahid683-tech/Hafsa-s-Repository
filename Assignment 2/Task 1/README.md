Bank Marketing Dataset Classification
Objective

The goal of this task is to predict whether a bank customer will subscribe to a term deposit using historical marketing campaign data. This involves analyzing the dataset, performing preprocessing, exploratory data analysis (EDA), building machine learning models, evaluating them, and extracting insights.

Dataset
Source: UCI Bank Marketing Dataset
Format: CSV (bank-full.csv)
Size: 45,211 records × 17 columns (approx.)
Target Column: y (yes=1, no=0)
Features: Customer demographics, banking info, campaign details, etc.
Approach
Dataset Loading: Loaded the dataset with pandas and checked its structure.
Data Cleaning: Removed duplicates, handled missing values, and cleaned column names.
Feature Encoding: Converted categorical variables using one-hot encoding.
Train-Test Split: Split data into 80% training and 20% testing using stratification.
Scaling: Applied StandardScaler for Logistic Regression.
Model Building:
Logistic Regression (scaled data)
Random Forest Classifier
Evaluation: Used Confusion Matrix, Classification Report, F1 Score, ROC-AUC, and ROC Curve visualization.
Feature Importance: Extracted top features from Random Forest.
Prediction Explanation: Used LIME to explain individual predictions.
Result Saving: Saved model comparison, feature importance, and LIME explanations for reporting.
Tools and Libraries
Python 3.x
Jupyter Notebook
Pandas, NumPy – Data manipulation
Matplotlib, Seaborn – Visualization
Scikit-learn – Machine learning models and evaluation metrics
LIME – Explainable AI for model predictions
Results and Findings
Target Distribution: Imbalanced classes; more “no” than “yes” responses.
Model Performance:
Model	F1 Score	ROC-AUC
Logistic Regression	0.72	0.78
Random Forest	0.79	0.85
Important Features (Top 5):
duration – Last contact duration
poutcome_success – Outcome of previous marketing campaign
month_may – Contact month
age – Customer age
balance – Customer balance
Insights:
Longer call durations and positive previous campaign outcomes significantly increase subscription likelihood.
Certain months (e.g., May, August) show higher subscription rates.
LIME explanations validate the contribution of these features for individual predictions.
Files in Repository
bank_marketing_classification.ipynb – Jupyter Notebook with complete analysis
bank-full.csv – Dataset (or a link if dataset is too large)
model_comparison.csv – Comparison of F1 and ROC-AUC scores
feature_importance.csv – Feature importance from Random Forest
lime_explanation_customer_1.html to lime_explanation_customer_5.html – LIME explanations
Conclusion

This task demonstrates a complete data science workflow: from data cleaning and exploration to model building, evaluation, and explainable predictions. Random Forest outperformed Logistic Regression in both F1 Score and ROC-AUC. The analysis provides actionable insights for targeted marketing campaigns.
