# Global Superstore Sales Dashboard and Business Analysis

## Objective

The objective of this task is to analyze the Global Superstore dataset and create useful business insights from sales, profit, customers, products, categories, regions, markets, and customer segments.

This project includes both data analysis and dashboard-based business reporting.

## Dataset

The dataset used in this task is the Global Superstore dataset.

It contains sales transaction records with information such as:

* Order ID
* Order Date
* Ship Date
* Customer Name
* Segment
* Region
* Market
* Category
* Sub-Category
* Product Name
* Sales
* Profit
* Quantity
* Discount
* Shipping Cost

## Approach

The following steps were performed:

1. Loaded the Global Superstore CSV dataset using pandas.
2. Cleaned column names and renamed columns for easier use.
3. Converted date columns into datetime format.
4. Converted sales, profit, quantity, discount, and shipping cost into numeric format.
5. Removed unreadable unnecessary columns if present.
6. Removed rows with missing important values.
7. Performed exploratory data analysis.
8. Calculated important KPIs such as total sales, total profit, total orders, total customers, profit margin, total quantity, average discount, and shipping cost.
9. Analyzed sales by region.
10. Analyzed sales by category.
11. Analyzed profit by sub-category.
12. Identified top customers by sales.
13. Analyzed segment-wise sales and profit.
14. Created monthly sales trend analysis.
15. Identified top products by sales.
16. Analyzed profit by market.
17. Generated business insights and recommendations.
18. Saved cleaned data and analysis result files.

## Tools and Libraries Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

## Key Performance Indicators

The following KPIs were calculated:

* Total Sales
* Total Profit
* Total Orders
* Total Customers
* Profit Margin
* Total Quantity
* Average Discount
* Total Shipping Cost

## Visualizations

The project includes the following visualizations:

* Number of orders by region
* Number of orders by category
* Number of orders by segment
* Sales distribution
* Profit distribution
* Sales by region
* Sales by category
* Profit by sub-category
* Top 5 customers by sales
* Sales and profit by segment
* Monthly sales trend
* Top 10 products by sales
* Profit by market

## Business Insights

The analysis helps identify:

* Best-performing region by sales
* Best-performing category by sales
* Top customer by sales
* Most profitable sub-category
* Best-performing market by profit
* Segment-wise sales and profit performance

## Suggested Business Actions

* Focus marketing campaigns on the highest-performing region.
* Give loyalty rewards to top customers.
* Promote profitable sub-categories more aggressively.
* Review low-profit or negative-profit sub-categories.
* Use segment-wise performance to target Consumer, Corporate, and Home Office customers separately.

## Streamlit Dashboard

This project also includes a Streamlit dashboard file.

To run the dashboard, use:

```bash
streamlit run app.py
```

The dashboard includes:

* Sidebar filters
* Dataset preview
* KPI cards
* Sales and profit charts
* Customer analysis
* Product analysis
* Business insights
* Download filtered data option

## Files in Repository

* `global_superstore_analysis.ipynb` - Jupyter Notebook containing full data analysis
* `app.py` - Streamlit dashboard application
* `Global Superstore.csv` - Original dataset
* `cleaned_global_superstore.csv` - Cleaned dataset
* `kpi_summary.csv` - KPI summary results
* `sales_by_region.csv` - Sales by region analysis
* `sales_by_category.csv` - Sales by category analysis
* `profit_by_subcategory.csv` - Profit by sub-category analysis
* `top_5_customers.csv` - Top customers by sales
* `segment_performance.csv` - Segment-wise sales and profit
* `monthly_sales_trend.csv` - Monthly sales trend
* `top_10_products.csv` - Top products by sales
* `profit_by_market.csv` - Profit by market analysis
* `README.md` - Project documentation

## Conclusion

This task demonstrates how business data analysis and dashboard visualization can be used to understand sales and profit performance.

The Global Superstore dataset was cleaned, analyzed, visualized, and summarized into useful business insights. The analysis can help improve marketing strategy, customer targeting, product promotion, and regional sales planning.
