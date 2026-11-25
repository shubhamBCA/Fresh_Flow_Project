# Final Business Insights

## 1. Overall Business Performance

- Total net revenue was ₹21,60,905.24.
- Total COGS was ₹10,62,934.27.
- Total gross profit was ₹10,97,970.97.
- Overall gross profit margin was 52.16%.
- A total of 22,465 units were sold.
- Average transaction value was ₹433.74.

**Observation:** The business made a good amount of profit during the 30 days. Its gross profit margin was 52.16%, which means that it earned around ₹52 as gross profit for every ₹100 of net revenue.

## 2. Product-wise Analysis

- Product 2 generated the highest net revenue of ₹3,79,811.06.
- It also had the highest gross profit of ₹1,93,528.65.
- Product 1 had the highest sales quantity, with 3,835 units sold.
- Product 7 had the highest gross profit margin of 60.97%.
- Product 6 had the lowest gross profit margin of 43.70%.

**Observation:** Product 2 performed best in terms of revenue and profit. Product 1 was sold the most, while Product 7 gave the highest profit percentage. Product 6 needs more attention because its profit margin was the lowest.

## 3. Outlet-wise Analysis

- Outlet 1 generated the highest revenue of ₹7,94,633.46.
- Outlet 1 also earned the highest gross profit of ₹4,04,759.59.
- It sold 8,309 units, which was the highest among all outlets.
- Outlet 3 received the highest average customer rating of 3.91.
- All three outlets had almost similar gross profit margins.

**Observation:** Outlet 1 performed best in sales and profit, while Outlet 3 had better customer ratings. We can study what Outlet 3 is doing well to improve customer experience at the other outlets.

## 4. Daily Sales Analysis

- Day 4 had the highest net revenue of ₹85,045.66.
- Day 3 had the lowest net revenue of ₹55,241.78.
- Average daily revenue was ₹72,030.17.
- Day 6 recorded the highest gross profit of ₹43,501.02.

**Observation:** Day 4 had the highest revenue, but Day 6 had the highest profit. This shows that the day with the highest sales is not always the day with the highest profit.

## 5. Discount Analysis

- The 10% discount was used the most, in 1,267 transactions.
- The 10% discount group generated the highest gross profit of ₹2,80,306.38.
- The 5% discount group had the highest average transaction value of ₹485.86.
- The 57% and 58% discount groups resulted in negative gross profit.

**Observation:** The 10% discount group performed well in terms of total gross profit. However, very high discounts may reduce profit. We should also remember that different discount groups have different numbers of transactions, so we cannot say that the discount alone caused these results.

## 6. Customer Rating Analysis

- The average customer rating was 3.84 out of 5.
- A total of 3,449 customers gave 4 or 5 stars.
- Around 69.30% of valid ratings were 4 or 5 stars.
- Outlet 3 had the highest average rating of 3.91.

**Observation:** Most customers gave positive ratings. Still, the business should look at the lower ratings to understand what problems customers are facing and how their experience can be improved.

## 7. Category-wise Analysis

- The Juice category generated the highest net revenue of ₹11,66,059.95.
- Juice also had the highest gross profit of ₹6,12,231.54.
- Lemonade had the highest gross profit margin of 60.97%.
- Smoothies had the lowest gross profit margin among the categories, at 45.17%.

**Observation:** Juice was the best-performing category in terms of total revenue and profit. Lemonade had the highest profit margin, which means it earned a higher percentage of profit compared to its revenue.

## 8. Data Quality Findings

During the data checking process, I found the following issues:

- 5 duplicated transaction ID values.
- 4 missing unit prices.
- 4 missing unit costs.
- 20 missing customer ratings.
- 4 invalid quantity records.
- 2 negative unit prices.
- 2 negative unit costs.
- 2 invalid discount records.
- 3 invalid customer ratings.
- 2 invalid outlet IDs.
- 4 product-category mismatches.

The 4 product-category mismatches were corrected using the product-category mapping provided in the assignment.

**Observation:** Data checking was important before starting the financial analysis. I kept the original dataset unchanged, corrected the category mismatches in the copied dataset, and excluded financially invalid records from financial calculations.

## 9. Suggestions for the Business

Based on the analysis, I would suggest the following:

1. The business should focus on Product 2 because it generated the highest revenue and gross profit.
2. Product 7 can be promoted more because it has the highest gross profit margin.
3. The business should check the cost and discount structure of Product 6 to understand why its profit margin is low.
4. Other outlets can learn from Outlet 1 because it performed well in sales and profit.
5. The business can study Outlet 3 to understand why it received better customer ratings.
6. High discount offers should be checked carefully because they can affect profit.
7. Data should be checked regularly to avoid missing values, duplicate IDs and incorrect entries.

## 10. Conclusion

In this project, I analysed 30 days of FreshFlow sales data using Python and NumPy. The business generated total net revenue of ₹21.61 lakh and gross profit of ₹10.98 lakh, with an overall gross profit margin of 52.16%.

From the analysis, I found that Product 2 and Outlet 1 performed best in terms of financial results. The Juice category generated the highest revenue, while Lemonade had the highest gross profit margin. I also analysed daily sales, discounts and customer ratings to understand the business performance.

During the project, I learned how to check data quality, identify incorrect records, apply NumPy operations, calculate business metrics and understand the results. This analysis helped me understand how data can be used to solve real-world business problems and support better decisions.