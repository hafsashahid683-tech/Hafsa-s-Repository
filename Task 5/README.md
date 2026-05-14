# Bank Marketing Prediction using Machine Learning (Logistic Regression)

## Project Overview
This project predicts whether a customer will subscribe to a bank term deposit based on demographic, financial, and campaign-related information.

The machine learning algorithm used is **Logistic Regression**, which is effective for binary classification tasks.

---

## Objective
The goals of this project are to:

- Load and inspect the bank marketing dataset
- Perform exploratory data analysis (EDA)
- Preprocess and encode data
- Train a Logistic Regression model
- Predict customer subscription outcomes
- Evaluate model performance
- Extract business insights from model coefficients

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

bank.csv

Alternative UCI version:

bank-additional-full.csv

---

## Project Workflow

### 1. Import Libraries
Used for:
- Data analysis
- Visualization
- Classification

### 2. Load Dataset
Dataset is loaded using Pandas.

### 3. Basic Exploration
Checks:
- Shape
- Columns
- Sample rows
- Target distribution

### 4. Exploratory Data Analysis
Visualizations include:
- Age distribution
- Job vs deposit subscription
- Marital status vs deposit subscription

### 5. Data Preprocessing
- Convert target values (yes/no → 1/0)
- One-hot encoding for categorical variables

### 6. Feature Selection
Separated:
- Features (X)
- Target (y)

### 7. Train-Test Split
- 80% Training
- 20% Testing

### 8. Model Training
Logistic Regression model is trained.

### 9. Prediction
Predicts whether customers subscribe.

### 10. Evaluation
Measured using:
- Accuracy
- Confusion Matrix
- Classification Report

### 11. Business Insight
Model coefficients identify:
- Positive influencers
- Negative influencers

---

## Expected Results
Outputs include:
- Prediction accuracy
- Confusion matrix
- Classification report
- Feature importance
- Business insights

---

## How to Run

### Step 1: Install Required Libraries
pip install pandas matplotlib seaborn scikit-learn

### Step 2: Place Dataset
Ensure:
bank.csv

is in the same notebook folder.

### Step 3: Run Notebook
Jupyter Notebook:
Kernel → Restart & Run All

---

## Common Errors

### FileNotFoundError
Cause:
Dataset not found

Solution:
Check:
- Correct file name
- Folder location

---

### KeyError
Cause:
Different target column name

Solution:
This project safely handles:
- deposit
- y

---

## Example Performance
Typical:
- Good accuracy for customer prediction
- Useful marketing insights

---

## Conclusion
This project demonstrates a complete machine learning classification workflow using Logistic Regression.

It helps understand:
- Data preprocessing
- One-hot encoding
- Customer analysis
- Classification
- Performance evaluation
- Business intelligence

## Author
Bank Marketing Prediction Project using Logistic Regression for beginner-friendly machine learning and business analytics practice.
