import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load the dataset
df = pd.read_csv("sales_data.csv")

# STEP 2: Display the complete dataset
print("===== SALES DATA =====")
print(df)

# STEP 3: Display first 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# STEP 4: Check dataset information
print("\n===== DATASET INFORMATION =====")
print(df.info())

# STEP 5: Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# STEP 6: Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# STEP 7: Total quantity sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# STEP 8: Product-wise sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)

# STEP 9: City-wise sales
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print("\n===== CITY-WISE SALES =====")
print(city_sales)

# STEP 10: Customer type sales
customer_sales = df.groupby("Customer_Type")["Sales"].sum()

print("\n===== CUSTOMER TYPE SALES =====")
print(customer_sales)

# STEP 11: Payment mode sales
payment_sales = df.groupby("Payment_Mode")["Sales"].sum()

print("\n===== PAYMENT MODE SALES =====")
print(payment_sales)

# STEP 12: Product quantity
product_quantity = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\n===== PRODUCT-WISE QUANTITY =====")
print(product_quantity)

# STEP 13: Product-wise sales chart
product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 14: City-wise sales chart
city_sales.plot(kind="bar")

plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
