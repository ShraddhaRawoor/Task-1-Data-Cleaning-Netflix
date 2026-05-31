import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# Convert date format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Remove extra spaces
text_cols = ["type", "director", "country", "rating"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Save cleaned dataset
df.to_csv("cleaned_netflix_titles.csv", index=False)

print("\nCleaning Completed")
print("Final Shape:", df.shape)
print("\nRemaining Missing Values:")
print(df.isnull().sum())