
import pandas as pd
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales.csv"

# Read the sales data
df = pd.read_csv(DATA_FILE)

# Calculate revenue, cost and profit
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["TotalCost"] = df["Quantity"] * df["UnitCost"]
df["Profit"] = df["Revenue"] - df["TotalCost"]

# Display business summary
print("\n--- SALES BUSINESS SUMMARY ---")
print("Total Revenue: Rs.", df["Revenue"].sum())
print("Total Cost: Rs.", df["TotalCost"].sum())
print("Total Profit: Rs.", df["Profit"].sum())
print("Number of Records:", len(df))
print("Total Items Sold:", df["Quantity"].sum())

# Revenue by product
print("\n--- REVENUE BY PRODUCT ---")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

# Revenue by region
print("\n--- REVENUE BY REGION ---")
print(df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

# Monthly revenue
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

print("\n--- MONTHLY REVENUE ---")
print(df.groupby("Month")["Revenue"].sum())

print("\nSales analysis completed successfully!")
