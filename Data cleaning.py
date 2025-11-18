import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("\nOriginal Data:")
print(df.head())

# ------------------------------
# 1. Handling Missing Values
# ------------------------------
df.fillna({
    "Age": df["Age"].median(),
    "Salary": df["Salary"].mean()
}, inplace=True)

print("\nAfter Handling Missing Values:")
print(df.head())

# ------------------------------
# 2. Removing Duplicates
# ------------------------------
df.drop_duplicates(inplace=True)

# ------------------------------
# 3. Converting Data Types
# ------------------------------
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

# ------------------------------
# 4. Normalizing Salary Column
# ------------------------------
df["Salary_Normalized"] = (df["Salary"] - df["Salary"].min()) / (df["Salary"].max() - df["Salary"].min())

# ------------------------------
# 5. Export Cleaned Data
# ------------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\nData Cleaning Completed Successfully!")
