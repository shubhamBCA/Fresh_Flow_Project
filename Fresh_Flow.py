from multiprocessing.reduction import duplicate
import numpy as np
import csv
with open("Data_Set/freshflow_sales.csv", "r", newline="") as ff_file:
    reader = csv.reader(ff_file)
    headers = next(reader)
    rows = list(reader)
ff_data = np.array(rows, dtype=float)
print("dataset loaded")
print("Shape:", ff_data.shape)
print("Number of rows:", ff_data.shape[0])
print("Number of columns:", ff_data.shape[1])
print("Dimensions", ff_data.ndim)
print("Data Type:", ff_data.dtype)
print(ff_data[:5])
print(headers)

for i, column in enumerate(headers):
    missing_count = np.sum(np.isnan(ff_data[:,i]))
    print(column, ":", missing_count)

for i, column in enumerate(headers):
    unique_values = np.unique(ff_data[:,i])
    print(column, ":", len(unique_values))

for i, column in enumerate(headers):
    print("\nColumn:", column)
    print("Minimum:", np.nanmin(ff_data[:,i]))
    print("Maximum:", np.nanmax(ff_data[:,i]))
    print("Mean:", np.nanmean(ff_data[:,i]))
    print("Median:", np.nanmedian(ff_data[:,i]))
    print("Standard Deviation:", np.nanstd(ff_data[:,i]))

transaction_id = ff_data[:,0]
unique_ids, counts = np.unique(
    transaction_id,
    return_counts=True
)
duplicate_id = unique_ids[counts>1]
print("Duplicate Transaction IDs:", duplicate_id)
print("Number of Duplicate IDs:", len(duplicate_id))

outlet_ids = ff_data[:, 2]
invalid_outlets = (outlet_ids < 1) | (outlet_ids > 3)
print("Invalid outlet records:", np.sum(invalid_outlets))

quantity = ff_data[:, 5]
invalid_quantity = quantity <= 0
print("Invalid quantity records:", np.sum(invalid_quantity))

unit_price = ff_data[:, 6]
invalid_price = (unit_price <= 0) & (~np.isnan(unit_price))
print("Invalid unit price:", np.sum(invalid_price))

unit_cost = ff_data[:, 7]
invalid_cost = (unit_cost <= 0) & (~np.isnan(unit_cost))
print("Invalid unit cost:", np.sum(invalid_cost))

discount = ff_data[:, 8]
invalid_discount = (discount < 0) | (discount > 1)
print("Invalid discount records:", np.sum(invalid_discount))

ff_stock = ff_data[:, 9]
negative_stock = ff_stock < 0
zero_stock = ff_stock == 0
print("Negative stock records:", np.sum(negative_stock))
print("Zero stock records:", np.sum(zero_stock))

product_code = ff_data[:, 3]
category_code = ff_data[:, 4]
product_category_mapping = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 4
}

expected_category = np.array([
    product_category_mapping[product]
    for product in product_code
])
category_mismatch = category_code != expected_category
print("Product-category mismatches:", np.sum(category_mismatch))
mismatched_records = ff_data[category_mismatch]
print(mismatched_records)

print("Transaction IDs:", mismatched_records[:, 0])
print("Product codes:", mismatched_records[:, 3])
print("Actual categories:", mismatched_records[:, 4])
print("Expected categories:", expected_category[category_mismatch])

payment_code = ff_data[:, 10]
invalid_payment = (payment_code < 1) | (payment_code > 4)
print("Invalid payment records:", np.sum(invalid_payment))

day_index = ff_data[:, 1]
invalid_days = (day_index < 1) | (day_index > 30)
print("Invalid day records:", np.sum(invalid_days))

for i, column in enumerate(headers):
    missing_count = np.sum(np.isnan(ff_data[:, i]))
    print(column, ":", missing_count)
total_missing = np.sum(np.isnan(ff_data))
print("Total missing values:", total_missing)

clean_data = ff_data.copy()
unit_price_index = headers.index("unit_price")
missing_price_mask = np.isnan(ff_data[:, unit_price_index])
missing_price_records = ff_data[missing_price_mask]
print("Records with missing unit prices:",missing_price_records)

unit_cost_index = headers.index("unit_cost")
missing_cost_mask = np.isnan(ff_data[:, unit_cost_index])
missing_cost_records = ff_data[missing_cost_mask]
print("Records with missing unit costs:",missing_cost_records)

clean_data = ff_data.copy()
print("Original shape:", ff_data.shape)
print("Clean data shape:", clean_data.shape)

product_code = clean_data[:, 3]
category_code = clean_data[:, 4]

expected_category = np.array([
    product_category_mapping[product]
    for product in product_code
])
category_mismatch = category_code != expected_category
print("Mismatches before correction:", np.sum(category_mismatch))
clean_data[category_mismatch, 4] = expected_category[category_mismatch]
print("Mismatches after correction:",np.sum(clean_data[:, 4] != expected_category))

outlet_ids = clean_data[:, 2]
invalid_outlet_mask = (outlet_ids < 1) | (outlet_ids > 3)
invalid_outlet_records = clean_data[invalid_outlet_mask]
print("Invalid outlet records:",invalid_outlet_records)
print("Invalid outlet records:",np.sum((clean_data[:, 2] < 1) | (clean_data[:, 2] > 3)))

quantity = clean_data[:, 5]
invalid_quantity_mask = quantity <= 0
invalid_quantity_records = clean_data[invalid_quantity_mask]
print("Invalid quantity count:", np.sum(invalid_quantity_mask))

unit_price = clean_data[:, 6]
invalid_price_mask = (unit_price <= 0) & (~np.isnan(unit_price))
invalid_price_records = clean_data[invalid_price_mask]
print("Invalid unit price records:",invalid_price_records)
print("Invalid unit prices:", np.sum(invalid_price_mask))

unit_cost = clean_data[:, 7]
invalid_cost_mask = (unit_cost <= 0) & (~np.isnan(unit_cost))
invalid_cost_records = clean_data[invalid_cost_mask]
print("Invalid unit cost records:",invalid_cost_records)
print("Invalid unit costs:", np.sum(invalid_cost_mask))

discount = clean_data[:, 8]
invalid_discount_mask = (discount < 0) | (discount > 1)
invalid_discount_records = clean_data[invalid_discount_mask]
print("Invalid discount records:",invalid_discount_records)
print("Invalid discount records:",np.sum(invalid_discount_mask))

rating = clean_data[:, 11]
invalid_rating_mask = (
    ((rating < 1) | (rating > 5)) & (~np.isnan(rating))
)
invalid_rating_records = clean_data[invalid_rating_mask]
print("Invalid rating records:",invalid_rating_records)
print("Invalid customer ratings:",np.sum(invalid_rating_mask))

unit_price = clean_data[:, 6]
high_price_mask = unit_price > 200
high_price_records = clean_data[high_price_mask]
print("Unusually high price records:",high_price_records)
print("Number of records:", np.sum(high_price_mask))

valid_prices = unit_price[~np.isnan(unit_price)]
print("Highest unit price:", np.max(valid_prices))
print("Top 10 unit prices:", np.sort(valid_prices)[-10:][::-1])

product_codes = clean_data[:, 3]
for product in np.unique(product_codes):
    prices = unit_price[product_codes == product]
    prices = prices[~np.isnan(prices)]
    print(
        "Product:", int(product),
        "| Minimum:", np.min(prices),
        "| Median:", np.median(prices),
        "| Maximum:", np.max(prices)
    )
suspicious_products = [4, 7]
for product in suspicious_products:
    mask = (
        (clean_data[:, 3] == product) &
        (clean_data[:, 6] > 100)
    )
    print("\nProduct:", product)
    print(clean_data[mask][:, [0, 3, 6]])

high_price_ids = [101468, 102005, 103950]
high_price_anomaly_mask = np.isin(
    clean_data[:, 0],
    high_price_ids
)
print("High-price anomalies flagged:",np.sum(high_price_anomaly_mask))

discount = clean_data[:, 8]
unique_discounts, discount_counts = np.unique(
    discount,
    return_counts=True
)

for value, count in zip(unique_discounts, discount_counts):
    print("Discount:", value, "| Count:", count)
discount = clean_data[:, 8]
high_discount_mask = (discount > 0.25) & (discount <= 1)
high_discount_records = clean_data[high_discount_mask]
print("High discount records:",high_discount_records)
print("Number of high discounts:",np.sum(high_discount_mask))

cleaning_summary = {
    "Product-category mismatches": 4,
    "Invalid outlet IDs": 2,
    "Invalid quantities": 4,
    "Invalid unit prices": 2,
    "Invalid unit costs": 2,
    "Invalid discounts": 2,
    "Invalid customer ratings": 3,
    "High unit-price anomalies": 3,
    "High discount anomalies": 5
}

for issue, count in cleaning_summary.items():
    print(issue, ":", count)
valid_transaction_mask = (
    (clean_data[:, 5] > 0) &
    (clean_data[:, 6] > 0) &
    (clean_data[:, 7] > 0) &
    (clean_data[:, 8] >= 0) &
    (clean_data[:, 8] <= 1)
)
print("Valid financial transactions:",np.sum(valid_transaction_mask))
print("Invalid financial transactions:",np.sum(~valid_transaction_mask))

missing_price_mask = np.isnan(clean_data[:, 6])
missing_cost_mask = np.isnan(clean_data[:, 7])
print("Missing unit prices:", np.sum(missing_price_mask))
print("Missing unit costs:", np.sum(missing_cost_mask))

financial_data = clean_data[
    valid_transaction_mask].copy()
print("Financial records:", len(financial_data))
print("Financial shape:", financial_data.shape)

quantity = financial_data[:, 5]
unit_price = financial_data[:, 6]
gross_sales = quantity * unit_price
print("Total Gross Sales:", round(np.sum(gross_sales),2))

discount_rate = financial_data[:, 8]
discount_amount = gross_sales * discount_rate
print("Total Discount Amount:", np.sum(discount_amount))

net_revenue = gross_sales - discount_amount
print("Total Net Revenue:", round(np.sum(net_revenue),2))

quantity = financial_data[:, 5]
unit_cost = financial_data[:, 7]
cogs = quantity * unit_cost
print("Total COGS:", np.sum(cogs))
gross_profit = net_revenue - cogs
print("Total Gross Profit:", round(np.sum(gross_profit),2))

gross_margin = (gross_profit / net_revenue) * 100
print("Overall Gross Profit Margin:", round(np.mean(gross_margin),2), "%")
overall_gross_margin = (
    np.sum(gross_profit) / np.sum(net_revenue)
) * 100
print("Overall Gross Profit Margin:", round(overall_gross_margin,2), "%")

average_transaction_value = np.mean(net_revenue)
print("Average Transaction Value:", round(average_transaction_value,2))

average_quantity = np.mean(financial_data[:, 5])
print("Average Quantity per Transaction:", round(average_quantity,2))

total_units_sold = np.sum(financial_data[:, 5])
print("Total Units Sold:", total_units_sold)

average_selling_price = np.sum(net_revenue) / total_units_sold
print("Average Selling Price per Unit:", round(average_selling_price,2))

average_cost_per_unit = np.sum(cogs) / total_units_sold
print("Average Cost per Unit:", round(average_cost_per_unit,2))

profit_per_unit = average_selling_price - average_cost_per_unit
print("Gross Profit per Unit:", profit_per_unit)

total_gross_sales = np.sum(gross_sales)
total_discount = np.sum(discount_amount)
discount_percentage = (total_discount / total_gross_sales) * 100
print("Overall Discount Percentage:", round(discount_percentage,2), "%")

product_codes = np.unique(financial_data[:, 3])

for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_revenue = np.sum(net_revenue[product_mask])
print("Product:", int(product),"| Net Revenue:", round(product_revenue, 2))

product_revenues = []
for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_revenue = np.sum(net_revenue[product_mask])
    product_revenues.append(product_revenue)
product_revenues = np.array(product_revenues)
best_index = np.argmax(product_revenues)
print("Best Product Code:", int(product_codes[best_index]))
print("Highest Net Revenue:", round(product_revenues[best_index], 2))

for product in product_codes:
    product_mask = financial_data[:, 3] == product
    total_quantity = np.sum(
        financial_data[product_mask, 5]
    )
print("Product:", int(product),"| Total Units Sold:", int(total_quantity))

product_quantities = []
for product in product_codes:
    product_mask = financial_data[:, 3] == product
    total_quantity = np.sum(
        financial_data[product_mask, 5]
    )
    product_quantities.append(total_quantity)
product_quantities = np.array(product_quantities)
best_quantity_index = np.argmax(product_quantities)
print("Best-Selling Product:", int(product_codes[best_quantity_index]))
print("Total Units Sold:", int(product_quantities[best_quantity_index]))

for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_profit = np.sum(gross_profit[product_mask])
    print("Product:", int(product),"| Gross Profit:", round(product_profit, 2))

product_profits = []
for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_profit = np.sum(gross_profit[product_mask])
    product_profits.append(product_profit)
product_profits = np.array(product_profits)
best_profit_index = np.argmax(product_profits)
print("Most Profitable Product:", int(product_codes[best_profit_index]))
print("Highest Gross Profit:", round(product_profits[best_profit_index], 2))

for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_revenue = np.sum(net_revenue[product_mask])
    product_profit = np.sum(gross_profit[product_mask])
    product_margin = (product_profit / product_revenue) * 100

    print("Product:", int(product),"| Gross Margin:", round(product_margin, 2), "%")

product_margins = []
for product in product_codes:
    product_mask = financial_data[:, 3] == product
    product_revenue = np.sum(net_revenue[product_mask])
    product_profit = np.sum(gross_profit[product_mask])
    product_margin = (product_profit / product_revenue) * 100
    product_margins.append(product_margin)
product_margins = np.array(product_margins)
best_margin_index = np.argmax(product_margins)
print("Highest Margin Product:", int(product_codes[best_margin_index]))
print("Highest Gross Margin:", round(product_margins[best_margin_index], 2), "%")

outlet_codes = np.unique(financial_data[:, 2])

for outlet in outlet_codes:
    outlet_mask = financial_data[:, 2] == outlet
    outlet_revenue = np.sum(net_revenue[outlet_mask])
    print("Outlet:", int(outlet),"| Net Revenue:", round(outlet_revenue, 2))

valid_outlet_mask = (
    (financial_data[:, 2] >= 1) &
    (financial_data[:, 2] <= 3)
)
valid_outlet_data = financial_data[valid_outlet_mask]
valid_outlet_revenue = net_revenue[valid_outlet_mask]
print("Valid Outlet Records:", len(valid_outlet_data))
print("Valid Outlet Revenue:",  round(np.sum(valid_outlet_revenue),2))
outlet_codes = np.array([1, 2, 3])

outlet_revenues = []
for outlet in outlet_codes:
    outlet_mask = valid_outlet_data[:, 2] == outlet
    revenue = np.sum(valid_outlet_revenue[outlet_mask])
    outlet_revenues.append(revenue)
outlet_revenues = np.array(outlet_revenues)
best_outlet_index = np.argmax(outlet_revenues)

print("Best Outlet:", int(outlet_codes[best_outlet_index]))
print("Highest Revenue:", round(outlet_revenues[best_outlet_index], 2))

for outlet in outlet_codes:
    outlet_mask = valid_outlet_data[:, 2] == outlet
    outlet_profit = np.sum(
        gross_profit[valid_outlet_mask][outlet_mask]
    )
    print("Outlet:", int(outlet),"| Gross Profit:", round(outlet_profit, 2))

for outlet in outlet_codes:
    outlet_mask = valid_outlet_data[:, 2] == outlet
    outlet_revenue = np.sum(
        valid_outlet_revenue[outlet_mask]
    )
    outlet_profit = np.sum(
        gross_profit[valid_outlet_mask][outlet_mask]
    )
    outlet_margin = (outlet_profit / outlet_revenue) * 100
    print("Outlet:", int(outlet),"| Gross Margin:", round(outlet_margin, 2), "%")

for outlet in outlet_codes:
    outlet_mask = valid_outlet_data[:, 2] == outlet
    total_quantity = np.sum(
        valid_outlet_data[outlet_mask, 5]
    )

    print("Outlet:", int(outlet),"| Total Units Sold:", int(total_quantity))
outlet_quantities = []

for outlet in outlet_codes:
    outlet_mask = valid_outlet_data[:, 2] == outlet
    total_quantity = np.sum(
        valid_outlet_data[outlet_mask, 5]
    )
    outlet_quantities.append(total_quantity)

outlet_quantities = np.array(outlet_quantities)
best_quantity_index = np.argmax(outlet_quantities)
print("Best-Selling Outlet:", int(outlet_codes[best_quantity_index]))
print("Total Units Sold:", int(outlet_quantities[best_quantity_index]))
day_indices = np.unique(financial_data[:, 1])

for day in day_indices:
    day_mask = financial_data[:, 1] == day
    daily_revenue = np.sum(net_revenue[day_mask])
    print("Day:", int(day),"| Net Revenue:", round(daily_revenue, 2))

daily_revenues = []

for day in day_indices:
    day_mask = financial_data[:, 1] == day
    daily_revenue = np.sum(net_revenue[day_mask])
    daily_revenues.append(daily_revenue)

daily_revenues = np.array(daily_revenues)
max_index = np.argmax(daily_revenues)
min_index = np.argmin(daily_revenues)

print("Highest Revenue Day:", int(day_indices[max_index]))
print("Highest Revenue:", round(daily_revenues[max_index], 2))

print("Lowest Revenue Day:", int(day_indices[min_index]))
print("Lowest Revenue:", round(daily_revenues[min_index], 2))

average_daily_revenue = np.mean(daily_revenues)

print("Average Daily Revenue:", round(average_daily_revenue, 2))

daily_profits = []
for day in day_indices:
    day_mask = financial_data[:, 1] == day
    daily_profit = np.sum(gross_profit[day_mask])
    daily_profits.append(daily_profit)
daily_profits = np.array(daily_profits)
print("Average Daily Gross Profit:", round(np.mean(daily_profits), 2))
max_profit_index = np.argmax(daily_profits)
min_profit_index = np.argmin(daily_profits)
print("Highest Profit Day:", int(day_indices[max_profit_index]))
print("Highest Daily Profit:", round(daily_profits[max_profit_index], 2))
print("Lowest Profit Day:", int(day_indices[min_profit_index]))
print("Lowest Daily Profit:", round(daily_profits[min_profit_index], 2))
discount_rates = np.unique(financial_data[:, 8])

for rate in discount_rates:
    discount_mask = financial_data[:, 8] == rate
    transaction_count = np.sum(discount_mask)
    print("Discount:", round(rate * 100, 2), "%","| Transactions:", transaction_count)

for rate in discount_rates:
    discount_mask = financial_data[:, 8] == rate
    discount_revenue = np.sum(net_revenue[discount_mask])
    print("Discount:", round(rate * 100, 2), "%","| Net Revenue:", round(discount_revenue, 2))

for rate in discount_rates:
    discount_mask = financial_data[:, 8] == rate
    average_revenue = np.mean(net_revenue[discount_mask])
    print("Discount:", round(rate * 100, 2), "%","| Average Transaction Value:", round(average_revenue, 2))

for rate in discount_rates:
    discount_mask = financial_data[:, 8] == rate
    discount_profit = np.sum(gross_profit[discount_mask])
    print("Discount:", round(rate * 100, 2), "%","| Gross Profit:", round(discount_profit, 2))

discount_profits = []
for rate in discount_rates:
    discount_mask = financial_data[:, 8] == rate
    discount_profit = np.sum(gross_profit[discount_mask])
    discount_profits.append(discount_profit)
discount_profits = np.array(discount_profits)
best_discount_index = np.argmax(discount_profits)
print("Most Profitable Discount Rate:",round(discount_rates[best_discount_index] * 100, 2), "%")
print("Highest Gross Profit:",round(discount_profits[best_discount_index], 2))
ratings = clean_data[:, 11]
average_rating = np.nanmean(
    ratings[(ratings >= 1) & (ratings <= 5)]
)
print("Average Customer Rating:",round(average_rating, 2))
ratings = clean_data[:, 11]
valid_ratings = ratings[
    (ratings >= 1) & (ratings <= 5)
]

unique_ratings, rating_counts = np.unique(
    valid_ratings,
    return_counts=True
)
for rating, count in zip(unique_ratings, rating_counts):
    print("Rating:", int(rating),"| Number of Customers:", count)
satisfied_customers = np.sum(valid_ratings >= 4)
total_valid_ratings = len(valid_ratings)
satisfaction_percentage = (
    satisfied_customers / total_valid_ratings
) * 100
print("Satisfied Customers:", satisfied_customers)
print("Customer Satisfaction:", round(satisfaction_percentage, 2), "%")
valid_rating_mask = (
    (clean_data[:, 11] >= 1) &
    (clean_data[:, 11] <= 5)
)
rating_data = clean_data[valid_rating_mask]
outlet_codes = np.array([1, 2, 3])
for outlet in outlet_codes:
    outlet_mask = rating_data[:, 2] == outlet
    outlet_ratings = rating_data[outlet_mask, 11]
    average_rating = np.mean(outlet_ratings)
    print("Outlet:", int(outlet),"| Average Rating:", round(average_rating, 2))
valid_rating_mask = (
    (clean_data[:, 11] >= 1) &
    (clean_data[:, 11] <= 5)
)
rating_data = clean_data[valid_rating_mask]
for product in product_codes:
    product_mask = rating_data[:, 3] == product
    product_ratings = rating_data[product_mask, 11]
    average_rating = np.mean(product_ratings)
    print("Product:", int(product),"| Average Rating:", round(average_rating, 2))

product_ratings = []
for product in product_codes:
    product_mask = rating_data[:, 3] == product
    average_rating = np.mean(
        rating_data[product_mask, 11]
    )
    product_ratings.append(average_rating)
product_ratings = np.array(product_ratings)
best_rating_index = np.argmax(product_ratings)
print("Highest Rated Product:", int(product_codes[best_rating_index]))
print("Average Rating:", round(product_ratings[best_rating_index], 2))
payment_codes = np.unique(clean_data[:, 10])
for payment in payment_codes:
    payment_mask = clean_data[:, 10] == payment
    transaction_count = np.sum(payment_mask)
    print("Payment Code:", int(payment),"| Transactions:", transaction_count)
payment_codes = np.unique(financial_data[:, 10])
for payment in payment_codes:
    payment_mask = financial_data[:, 10] == payment
    payment_revenue = np.sum(net_revenue[payment_mask])
    print("Payment Code:", int(payment),"| Net Revenue:", round(payment_revenue, 2))

payment_counts = []
for payment in payment_codes:
    payment_mask = financial_data[:, 10] == payment
    transaction_count = np.sum(payment_mask)
    payment_counts.append(transaction_count)
payment_counts = np.array(payment_counts)
best_payment_index = np.argmax(payment_counts)
print("Most Used Payment Code:",int(payment_codes[best_payment_index]))
print("Total Transactions:",
      int(payment_counts[best_payment_index]))
for payment in payment_codes:
    payment_mask = financial_data[:, 10] == payment
    payment_profit = np.sum(gross_profit[payment_mask])
    print("Payment Code:", int(payment),"| Gross Profit:", round(payment_profit, 2))
for payment in payment_codes:
    payment_mask = financial_data[:, 10] == payment
    payment_revenue = np.sum(net_revenue[payment_mask])
    payment_profit = np.sum(gross_profit[payment_mask])
    payment_margin = (payment_profit / payment_revenue) * 100
    print("Payment Code:", int(payment),"| Gross Margin:", round(payment_margin, 2), "%")

category_codes = np.unique(financial_data[:, 4])
for category in category_codes:
    category_mask = financial_data[:, 4] == category
    category_revenue = np.sum(net_revenue[category_mask])
    print("Category:", int(category),"| Net Revenue:", round(category_revenue, 2))
for category in category_codes:
    category_mask = financial_data[:, 4] == category
    category_profit = np.sum(gross_profit[category_mask])
    print("Category:", int(category),"| Gross Profit:", round(category_profit, 2))

category_margins = []
for category in category_codes:
    category_mask = financial_data[:, 4] == category
    category_revenue = np.sum(net_revenue[category_mask])
    category_profit = np.sum(gross_profit[category_mask])
    category_margin = (
        category_profit / category_revenue
    ) * 100
    category_margins.append(category_margin)
category_margins = np.array(category_margins)
best_category_index = np.argmax(category_margins)
print("Highest Margin Category:",int(category_codes[best_category_index]))
print("Highest Gross Margin:",round(category_margins[best_category_index], 2), "%")

calculated_profit = np.sum(net_revenue) - np.sum(cogs)
actual_profit = np.sum(gross_profit)
print("Calculated Gross Profit:", round(calculated_profit, 2))
print("Actual Gross Profit:", round(actual_profit, 2))
print("Validation:",np.isclose(calculated_profit, actual_profit))

calculated_revenue = np.sum(gross_sales) - np.sum(discount_amount)
actual_revenue = np.sum(net_revenue)
print("Calculated Net Revenue:", round(calculated_revenue, 2))
print("Actual Net Revenue:", round(actual_revenue, 2))
print("Validation:",np.isclose(calculated_revenue, actual_revenue))

total_units = np.sum(financial_data[:, 5])
product_units_total = np.sum(product_quantities)
print("Total Units from Dataset:", total_units)
print("Total Units from Product Analysis:", product_units_total)
print("Validation:",np.isclose(total_units, product_units_total))

product_revenue_total = np.sum(product_revenues)
total_net_revenue = np.sum(net_revenue)
print("Product-wise Revenue Total:",round(product_revenue_total, 2))
print("Overall Net Revenue:",round(total_net_revenue, 2))
print("Validation:",np.isclose(product_revenue_total, total_net_revenue))