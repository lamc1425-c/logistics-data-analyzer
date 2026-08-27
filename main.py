# Import pandas and assign it the alias "pd"
import pandas as pd

# Load order data from CSV
df = pd.read_csv("data/orders.csv")

# Inspect the initial DataFrame
print(df.head())
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())

# Standardize city names
df["city"] = df["city"].str.title()

# Verify city name transformation
print(df["city"])

# Clean and standardize status values
df["status"] = df["status"].str.strip().str.title()

# Verify status transformation
print(df["status"])

# Check duplicate order entries
print(df[df["order_id"] == "ORD-003"])

# Check the duplicate rows in the dataset
print(df.duplicated())