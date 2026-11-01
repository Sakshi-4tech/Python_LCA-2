
import pandas as pd

# Load the dataset
df = pd.read_csv("Iris.csv")

# Display dataset
print("First five rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["SepalWidthCm"] = df["SepalWidthCm"].fillna(df["SepalWidthCm"].mean())
df = df.dropna()

# Check and remove duplicates
print("\nDuplicate Records:")
print(df.duplicated().sum())
df = df.drop_duplicates()

# Remove unnecessary column
if "Id" in df.columns:
    df = df.drop("Id", axis=1)

# Select data using loc
print("\nSetosa Flowers:")
print(df.loc[df["Species"] == "Iris-setosa"])

# Display cleaned dataset
print("\nFinal Cleaned Dataset:")
print(df.head())

print("\nFinal Dataset Shape:", df.shape)
