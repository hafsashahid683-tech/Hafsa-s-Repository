# Household Power Consumption Forecasting

## Objective

The objective of this task is to forecast household electricity consumption using time series forecasting and machine learning models.

The target variable used for forecasting is `Global_active_power`.

Three models were used:

* ARIMA
* Prophet
* XGBoost

The models were evaluated and compared using MAE and RMSE.

## Dataset

The dataset used in this task is the Household Power Consumption dataset.

The original dataset contains household electricity consumption recorded at minute-level frequency.

Important columns include:

* Date
* Time
* Global_active_power
* Global_reactive_power
* Voltage
* Global_intensity
* Sub_metering_1
* Sub_metering_2
* Sub_metering_3

For this task, `Global_active_power` was selected as the main energy usage column.

## Approach

The following steps were performed:

1. Loaded the dataset using pandas.
2. Parsed Date and Time columns into a single Datetime column.
3. Set Datetime as the index.
4. Selected `Global_active_power` as the target variable.
5. Converted the target column into numeric format.
6. Handled missing values using interpolation.
7. Resampled minute-level data into hourly average usage.
8. Visualized household energy usage over time.
9. Created time-based features for XGBoost.
10. Created lag features and rolling mean features.
11. Split the data using the last 7 days as test data.
12. Trained ARIMA, Prophet, and XGBoost models.
13. Evaluated models using MAE and RMSE.
14. Compared actual and forecasted values using visualization.
15. Saved model comparison and forecast results as CSV files.

## Tools and Libraries Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Statsmodels
* Prophet
* XGBoost

## Models Used

### ARIMA

ARIMA is a statistical forecasting model used for time series data. It predicts future values based on past values and trends.

### Prophet

Prophet is a time series forecasting model that handles seasonality and trend patterns.

### XGBoost

XGBoost is a machine learning regression model. In this task, it used time-based features, lag values, and rolling averages to forecast energy consumption.

## Evaluation Metrics

The models were evaluated using:

* MAE: Mean Absolute Error
* RMSE: Root Mean Squared Error

Lower MAE and RMSE values indicate better model performance.

## Results and Findings

The models were compared using MAE and RMSE.

The final comparison was saved in:

`model_comparison_results.csv`

The forecasted values were saved in:

`energy_forecast_results.csv`

The model with the lowest MAE and RMSE is considered the best forecasting model for this task.

## Files in Repository

* `household_power_forecasting.ipynb` - Jupyter Notebook containing complete analysis and forecasting
* `household_power_consumption.txt` - Original dataset
* `model_comparison_results.csv` - Model evaluation comparison
* `energy_forecast_results.csv` - Actual and forecasted values
* `README.md` - Project documentation

## Conclusion

This task demonstrates how time series forecasting can be used to predict household electricity consumption.

The data was cleaned, resampled, explored, and modeled using ARIMA, Prophet, and XGBoost. The results provide useful insights into energy usage patterns and can support better electricity demand planning.
