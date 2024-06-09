import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataframe yang sudah dibersihkan
df = pd.read_csv('clean_data.csv')

# Analisis sales by product
sales_by_product = df.groupby('product_name')['quantity'].sum().reset_index()
print(sales_by_product)

# Visualisasi sales by product
plt.figure(figsize=(16, 12))
sns.barplot(x='product_name', y='quantity', data=sales_by_product, palette='viridis')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.xticks(rotation='vertical', size=8)
plt.ylabel('Quantity')
plt.show()

# Analisis sales by months
df['order_date'] = pd.to_datetime(df['order_date'])
df['month_date'] = df['order_date'].dt.month

sales_by_month = df.groupby('month_date')['quantity'].sum().reset_index()
print(sales_by_month)

# Visualisasi sales by Months
plt.figure(figsize=(10, 6))
plt.plot('month_date', 'quantity', data=sales_by_month, color='skyblue', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales by Month')
plt.grid(True)
plt.show()

# Menghitung Total Revenue per Bulan
revenue_per_month= df.groupby('month_date')['amount'].sum().reset_index()
print(revenue_per_month)

# Visualisasi hubungan antara total penjualan dengan total revenue
plt.figure(figsize=(12, 6))
plt.plot('month_date', 'quantity', data=sales_by_month, color='skyblue', linestyle='-')
plt.plot('month_date', 'amount', data=revenue_per_month, color='green', linestyle='-')
plt.title('Sales and Revenue per Month')
plt.xlabel('Month')
plt.ylabel('Total')
plt.grid(True)
plt.legend()
plt.show()

# Mencari produk dengan penjualan tertinggi setiap bulannya
monthly_product_sales = df.groupby(['month_date', 'product_name'])['quantity'].sum().reset_index()
idx = monthly_product_sales.groupby(['month_date'])['quantity'].idxmax()
highest_sales_each_month = monthly_product_sales.loc[idx]
print(highest_sales_each_month)

# Visualisasi 
plt.figure(figsize=(12, 6))
sns.barplot(x='month_date', y='quantity', hue='product_name', data=highest_sales_each_month, dodge=False)
plt.title('Top Product Every Month')
plt.xlabel('Month')
plt.ylabel('Quantity')
plt.legend(title='Nama Produk', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


