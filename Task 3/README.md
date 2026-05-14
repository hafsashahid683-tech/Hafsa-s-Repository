# Customer Churn Prediction using Machine Learning (Random Forest Classifier)

## Project Overview
This project predicts whether a customer will leave a bank (churn) or remain with the bank based on customer information such as age, geography, balance, credit score, and tenure.

The machine learning model used is **Random Forest Classifier**, which is highly effective for classification tasks and feature importance analysis.

---

## Objective
The goals of this project are to:

- Load and inspect customer churn data
- Clean and preprocess the dataset
- Encode categorical variables
- Perform exploratory data analysis (EDA)
- Train a Random Forest model
- Predict customer churn
- Evaluate model performance
- Analyze feature importance

---

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Dataset
Dataset file used:

Churn_Modelling.csv

---

## Project Workflow

### 1. Import Libraries
Libraries for:
- Data analysis
- Visualization
- Machine learning

### 2. Load Dataset
Dataset is loaded using Pandas.

### 3. Dataset Overview
Checks:
- Dataset shape
- Columns
- Missing values
- Sample rows

### 4. Data Cleaning
Removed unnecessary columns:
- RowNumber
- CustomerId
- Surname

### 5. Encoding
Converted categorical columns:
- Geography
- Gender

Using one-hot encoding.

### 6. Exploratory Data Analysis
Visualizations include:
- Age distribution
- Balance distribution
- Customer churn count

### 7. Feature Selection
Separated:
- Features (X)
- Target (y)

### 8. Train-Test Split
- 80% Training
- 20% Testing

### 9. Model Training
Random Forest Classifier is trained.

### 10. Prediction
Model predicts customer churn.

### 11. Evaluation
Measured using:
- Accuracy Score
- Confusion Matrix
- Classification Report

### 12. Feature Importance
Identifies key variables affecting churn.

---

## Expected Results
Outputs include:
- Accuracy score
- Confusion matrix
- Classification report
- Feature importance ranking
- Visual charts

---

## How to Run

### Step 1: Install Libraries
pip install pandas matplotlib seaborn scikit-learn

### Step 2: Place Dataset
Ensure:
Churn_Modelling.csv

is in the same folder as the notebook.

### Step 3: Run Notebook
Jupyter Notebook:
Kernel → Restart & Run All

---

## Common Errors

### FileNotFoundError
Cause:
Dataset not found

Solution:
Check file name and location

---

### KeyError
Cause:
Column names may differ

Solution:
Check:
print(df.columns)

---

## Example Performance
Typical accuracy:
80% to 87%

(Depends on dataset quality and preprocessing.)

---

## Conclusion
This project demonstrates a full machine learning classification pipeline using Random Forest.

It helps understand:
- Data preprocessing
- One-hot encoding
- EDA
- Classification
- Performance metrics
- Feature importance

---

## Future Improvements
- Hyperparameter tuning
- Cross-validation
- XGBoost / Gradient Boosting
- Deployment using Flask or Streamlit

---

## Author
Customer Churn Prediction Project using Random Forest Classifier for beginner-friendly machine learning practice.
