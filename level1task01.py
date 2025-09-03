import pandas as pd

# Load dataset
df = pd.read_csv("2) Stock Prices Data Set.csv")

print(" Original Dataset:")
print(df.head())

# 1. Check for null values
print("\n🔎 Null values in each column:")
print(df.isnull().sum())

# 2. Handle missing values
# Example: fill numeric NaN with mean, text NaN with "UNKNOWN"
df['open'] = df['open'].fillna(df['open'].mean())
df['high'] = df['high'].fillna(df['high'].mean())
df['low'] = df['low'].fillna(df['low'].mean())
df['close'] = df['close'].fillna(df['close'].mean())
df['volume'] = df['volume'].fillna(df['volume'].median())   # median for skewed data
df['symbol'] = df['symbol'].fillna("UNKNOWN")

# 3. Capitalize text columns
df['symbol'] = df['symbol'].str.upper()

# 4. Format date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 5. Show cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

# 6. Save cleaned dataset
df.to_csv("cleaned_stock_dataset.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_stock_dataset.csv'")
