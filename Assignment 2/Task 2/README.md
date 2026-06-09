# Customer Segmentation using K-Means Clustering

## Objective

The objective of this task is to segment mall customers into different groups based on their annual income and spending score.

Customer segmentation helps businesses understand customer behavior and create targeted marketing strategies for different customer groups.

## Dataset

The dataset used in this task is the Mall Customers Dataset.

It contains customer information such as:

* Customer ID
* Gender
* Age
* Annual Income
* Spending Score

The main features used for clustering are:

* Annual Income
* Spending Score

## Approach

The following steps were performed in this task:

1. Loaded the Mall Customers dataset using pandas.
2. Checked dataset shape, column names, missing values, and statistical summary.
3. Renamed columns for easier use.
4. Performed exploratory data analysis using charts and plots.
5. Selected Annual Income and Spending Score as clustering features.
6. Scaled the selected features using StandardScaler.
7. Used the elbow method to find a suitable number of clusters.
8. Calculated silhouette scores to evaluate clustering performance.
9. Applied K-Means Clustering with 5 clusters.
10. Visualized customer segments using scatter plots.
11. Used PCA for additional cluster visualization.
12. Analyzed each cluster and suggested marketing strategies.
13. Saved the final clustered dataset as a CSV file.

## Tools and Libraries Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Results and Findings

The K-Means model divided customers into 5 different segments based on their income and spending behavior.

The customer segments included:

* High Income, High Spending customers
* High Income, Low Spending customers
* Low Income, High Spending customers
* Low Income, Low Spending customers
* Average Income, Average Spending customers

These segments can help businesses design better marketing campaigns for different customer groups.

## Marketing Insights

* High-income and high-spending customers can be targeted with premium products, VIP memberships, and luxury offers.
* High-income but low-spending customers can be encouraged through personalized offers and loyalty rewards.
* Low-income but high-spending customers can be targeted with budget-friendly bundles and seasonal discounts.
* Low-income and low-spending customers can be targeted through basic discount campaigns and awareness promotions.
* Average customers can be targeted using regular promotions and loyalty points.

## Files in Repository

* `customer_segmentation_kmeans.ipynb` - Jupyter Notebook containing full analysis and clustering model
* `Mall_Customers.csv` - Original dataset
* `Mall_Customers_Clustered.csv` - Final dataset with cluster labels
* `README.md` - Project documentation

## Conclusion

This task demonstrates how unsupervised machine learning can be used for customer segmentation.

K-Means Clustering successfully grouped customers into meaningful segments based on annual income and spending score. These insights can support better business decisions and targeted marketing strategies.
