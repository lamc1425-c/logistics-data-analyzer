# 1. Import pandas and assign it the alias "pd"
import pandas as pd

# 2. Load the dataset using a relative path
df = pd.read_csv("data/orders.csv")

# 3. Display the first few rows
print(df.head())

# 4. Display the total numbers of rows and columns
print(df.shape)

# 5. Display the names of all columns
print(df.columns)

# 6. Display the data type of each column
print(df.dtypes)

# 7. Count total missing (empty) values per column
print(df.isnull().sum())


df["city"] = df["city"].str.title()

print(df["city"])

df["status"] = df["status"].str.strip().str.title()

print(df["status"])