# Medical Insurance Cost Prediction using Machine Learning (Linear Regression)

## Project Overview
This project predicts medical insurance charges based on customer attributes such as age, BMI, smoking status, sex, number of children, and region.

The machine learning model used is **Linear Regression**, which predicts continuous values like insurance charges.

---

## Objective
The goals of this project are to:

- Load and inspect the insurance dataset
- Explore relationships between variables
- Visualize important patterns
- Encode categorical variables
- Train a Linear Regression model
- Predict insurance charges
- Evaluate prediction accuracy

---

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## Dataset
Dataset file used:

insurance.csv

---

## Project Workflow

### 1. Import Libraries
Libraries used for:
- Data analysis
- Visualization
- Regression modeling

### 2. Load Dataset
Dataset is loaded using Pandas.

### 3. Dataset Overview
Checks:
- Shape
- Columns
- Missing values
- Sample rows

### 4. Exploratory Data Analysis (EDA)
Visualizations include:
- Age vs Charges
- BMI vs Charges
- Smoking Status vs Charges

### 5. Encoding
Categorical columns are converted into numerical format using one-hot encoding.

### 6. Feature Selection
Separated:
- Features (X)
- Target (y)

### 7. Train-Test Split
- 80% Training
- 20% Testing

### 8. Model Training
Linear Regression model is trained.

### 9. Prediction
Insurance charges are predicted.

### 10. Evaluation
Measured using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## Expected Results
Outputs include:
- Insurance charge predictions
- MAE
- RMSE
- Visual graphs
- Actual vs Predicted comparison

---

## How to Run

### Step 1: Install Required Libraries
pip install pandas matplotlib seaborn scikit-learn numpy

### Step 2: Place Dataset
Ensure:
insurance.csv

is in the same folder as your notebook.

### Step 3: Run Notebook
Jupyter Notebook:
Kernel → Restart & Run All

---

## Common Errors

### FileNotFoundError
Cause:
Dataset file not found

Solution:
Check:
- Correct file name
- Correct folder location

---

### KeyError
Cause:
Column names may differ

Solution:
Run:
print(df.columns)

---

## Example Performance
Typical:
- Low MAE = Better accuracy
- Low RMSE = Better prediction performance

---

## Conclusion
This project demonstrates a complete machine learning regression workflow using Linear Regression.

It helps understand:
- Data preprocessing
- Visualization
- One-hot encoding
- Regression analysis
- Performance evaluation
