import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================
# STEP 1 - LOAD DATA
# ============================================================
df = pd.read_excel("Online Retail.xlsx")

print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types & Null Info:")
print(df.info())

print("\nMissing Values per Column:")
print(df.isnull().sum())

# ============================================================
# STEP 2 - DATA CLEANING
# ============================================================

# Check duplicates before removing
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where Description is empty
df = df.dropna(subset=["Description"])

# Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Remove rows with negative or zero Quantity
df = df[df['Quantity'] > 0]

# Remove rows with negative or zero UnitPrice
df = df[df['UnitPrice'] > 0]

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("\nCleaned Data Shape:", df.shape)
print("\nCleaned Data Sample:")
print(df.head())

# ============================================================
# STEP 3 - CREATE FOLDER TO SAVE CHARTS
# ============================================================
os.makedirs("charts", exist_ok=True)

# ============================================================
# STEP 4 - CHART 1 : MONTHLY REVENUE TREND
# ============================================================

# Extract Month from InvoiceDate
df["Month"] = df["InvoiceDate"].dt.to_period("M")

# Group by Month and sum Revenue
monthly_sales = df.groupby("Month")["Revenue"].sum()

# Plot
plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.show()

# ============================================================
# STEP 5 - CHART 2 : TOP 10 SELLING PRODUCTS
# ============================================================

# Group by product name and sum Quantity
top_products = df.groupby("Description")["Quantity"].sum()
top_products = top_products.sort_values(ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 5))
top_products.plot(kind="bar")
plt.title("Top 10 Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()

# ============================================================
# STEP 6 - CHART 3 : TOP 10 COUNTRIES BY REVENUE
# ============================================================

# Group by Country and sum Revenue
country_sales = df.groupby("Country")["Revenue"].sum()
country_sales = country_sales.sort_values(ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 5))
country_sales.plot(kind="bar")
plt.title("Top Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("charts/top_countries.png")
plt.show()

# ============================================================
# STEP 7 - CHART 4 : REVENUE DISTRIBUTION
# ============================================================

# Filter only orders below £500 to remove extreme outliers
plt.figure(figsize=(10, 5))
df[df["Revenue"] < 500]["Revenue"].hist(bins=50)
plt.title("Revenue Distribution (Orders below £500)")
plt.xlabel("Revenue (£)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("charts/revenue_distribution.png")
plt.show()

# ============================================================
# STEP 8 - PRINT KEY STATS
# ============================================================
print("\n============ KEY STATS ============")
print("Total Revenue: £", round(df["Revenue"].sum(), 2))
print("Total Orders:", df["InvoiceNo"].nunique())
print("Total Products:", df["Description"].nunique())
print("Total Countries:", df["Country"].nunique())
print("Date Range:", df["InvoiceDate"].min(), "to", df["InvoiceDate"].max())
print("Top Country:", country_sales.index[0])
print("Best Month:", str(monthly_sales.idxmax()))
print("===================================")