import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('shopping_data.csv')

# Data Preprocessing
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Monthly Sales Trend
monthly_sales = df.groupby(['Year', 'Month'])['Quantity'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Quantity', hue='Year', data=monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Quantity Sold')
plt.show()

# Popular Products
product_sales = df.groupby('Product')['Quantity'].sum().reset_index()
product_sales = product_sales.sort_values(by='Quantity', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='Quantity', y='Product', data=product_sales.head(10), palette='viridis')
plt.title('Top 10 Popular Products')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product')
plt.show()

# Customer Behavior Analysis
customer_spending = df.groupby('CustomerID')['Price'].sum().reset_index()
customer_spending = customer_spending.sort_values(by='Price', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='Price', y='CustomerID', data=customer_spending.head(10), palette='magma')
plt.title('Top 10 Customers by Spending')
plt.xlabel('Total Spending')
plt.ylabel('Customer ID')
plt.show()

# Save Results
monthly_sales.to_csv('monthly_sales.csv', index=False)
product_sales.to_csv('popular_products.csv', index=False)
customer_spending.to_csv('customer_spending.csv', index=False)