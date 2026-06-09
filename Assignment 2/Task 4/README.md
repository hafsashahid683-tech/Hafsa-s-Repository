# Loan Default Prediction with Cost-Based Threshold Optimization

## Objective

The objective of this task is to predict whether a customer is likely to default on a loan.

This project uses machine learning models to classify loan default risk and applies cost-based threshold optimization to reduce business loss.

The models used are:

* Logistic Regression
* CatBoost Classifier

## Dataset

The dataset used in this task is a credit risk dataset.

The target column is:

* `loan_status`

The dataset contains customer and loan-related features that are used to predict whether a customer may default on a loan.

## Approach

The following steps were performed:

1. Loaded the credit risk dataset using pandas.
2. Checked dataset shape, information, and target distribution.
3. Dropped ID column if present.
4. Separated features and target variable.
5. Identified numeric and categorical columns.
6. Handled missing values using median and mode.
7. Performed exploratory data analysis.
8. Encoded categorical variables using one-hot encoding.
9. Split the dataset into training and testing sets.
10. Scaled data for Logistic Regression.
11. Trained Logistic Regression model.
12. Trained CatBoost Classifier model.
13. Evaluated models using ROC-AUC, confusion matrix, and classification report.
14. Defined business costs for false positives and false negatives.
15. Applied cost-based threshold optimization.
16. Evaluated models again using the best threshold.
17. Plotted cost vs threshold.
18. Plotted ROC curves.
19. Extracted CatBoost feature importance.
20. Saved final result files.

## Tools and Libraries Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* CatBoost

## Models Used

### Logistic Regression

Logistic Regression was used as a baseline classification model. It was trained using scaled features and balanced class weights.

### CatBoost Classifier

CatBoost was used as an advanced machine learning model. It was trained to predict loan default probability and also used to calculate feature importance.

## Business Cost Strategy

In loan default prediction, different prediction errors have different business costs.

False Positive:

* The model predicts default, but the customer would not default.
* The business may reject a good customer.

False Negative:

* The model predicts no default, but the customer actually defaults.
* The business may give a loan to a risky customer.

In this task:

* False Positive Cost = 1
* False Negative Cost = 10

Since false negatives are more costly, threshold optimization was used to reduce total business cost.

## Evaluation Metrics

The models were evaluated using:

* ROC-AUC Score
* Confusion Matrix
* Classification Report
* Business Cost
* Cost-Based Best Threshold

## Results and Findings

The models were compared using ROC-AUC and business cost.

Cost-based threshold optimization helped identify the best decision threshold for reducing business loss.

The final outputs were saved in CSV files:

* `logistic_threshold_cost_results.csv`
* `catboost_threshold_cost_results.csv`
* `catboost_feature_importance.csv`

## Files in Repository

* `loan_default_prediction.ipynb` - Jupyter Notebook containing full analysis and model building
* `Credit Risk Dataset.csv` - Dataset file
* `logistic_threshold_cost_results.csv` - Threshold cost results for Logistic Regression
* `catboost_threshold_cost_results.csv` - Threshold cost results for CatBoost
* `catboost_feature_importance.csv` - CatBoost feature importance results
* `README.md` - Project documentation

## Conclusion

This task demonstrates how machine learning can be used for loan default prediction.

Logistic Regression and CatBoost were trained and evaluated. Cost-based threshold optimization was applied to select the decision threshold that minimizes total business cost.

This approach is useful in financial risk management because it considers both model performance and business impact.
