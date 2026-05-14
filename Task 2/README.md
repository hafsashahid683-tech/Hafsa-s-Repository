Loan Prediction using Machine Learning (Logistic Regression)
Project Overview

This project uses Machine Learning to predict whether a loan application will be approved or rejected based on applicant details such as income, education, loan amount, and other related factors.

The model used in this project is Logistic Regression, a popular classification algorithm suitable for binary outcomes like loan approval status.

Objective

The main objective of this project is to:

Load and explore the loan prediction dataset
Clean missing values
Perform exploratory data analysis (EDA)
Convert categorical data into numerical format
Train a Logistic Regression model
Predict loan approval status
Evaluate model performance
Technologies Used
Python
Pandas
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook
Dataset

The dataset file used in this project is:

loan-prediction-dataset.csv

Make sure the dataset file is in the same folder as your Jupyter Notebook.

Project Workflow
1. Import Libraries

Necessary libraries for data analysis, visualization, preprocessing, and machine learning are imported.

2. Load Dataset

The dataset is loaded using Pandas:

df = pd.read_csv("loan-prediction-dataset.csv")
3. Dataset Overview

The project checks:

Shape of dataset
Column names
First few rows
Missing values
4. Data Cleaning

Missing values are handled using:

Mode for categorical columns
Median for numerical columns
5. Exploratory Data Analysis (EDA)

Visualizations include:

Loan Amount Distribution
Education Distribution
Applicant Income Distribution
6. Encoding

Categorical columns are converted into numerical values using Label Encoding.

7. Feature Selection

Features (X) and target variable (y) are separated.

8. Train-Test Split

Data is divided into:

80% Training Data
20% Testing Data
9. Model Training

A Logistic Regression model is trained on the training data.

10. Prediction

Predictions are made on test data.

11. Evaluation

Model performance is measured using:

Accuracy Score
Confusion Matrix
Classification Report
Expected Output

The project provides:

Cleaned dataset
Data visualizations
Model accuracy
Confusion matrix
Classification report
Example Results

Typical evaluation metrics may include:

Accuracy: ~75% to 85%

(Actual accuracy depends on dataset quality.)

How to Run the Project
Step 1:

Install required libraries:

pip install pandas matplotlib seaborn scikit-learn
Step 2:

Place loan-prediction-dataset.csv in the same folder as the notebook.

Step 3:

Run all cells in Jupyter Notebook:

Kernel → Restart & Run All
Common Errors and Solutions
Error:
FileNotFoundError
Solution:

Check dataset file name and folder location.

Error:
NameError: df is not defined
Solution:

Make sure dataset loads successfully before running other cells.

Conclusion

This project demonstrates a complete machine learning workflow from data preprocessing to model evaluation using Logistic Regression.

It is a beginner-friendly classification project that helps understand:

Data cleaning
EDA
Label Encoding
Model training
Performance evaluation
