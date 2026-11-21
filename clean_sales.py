from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
source = ROOT / "data" / "sales.csv"
target = ROOT / "data" / "cleaned_sales.csv"

df = pd.read_csv(source)
df.columns = [c.strip() for c in df.columns]
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df = df.drop_duplicates()
df = df.dropna(subset=["Order ID", "Order Date", "Sales", "Category", "Region", "Product"])
df["Order ID"] = df["Order ID"].astype(int)
df["Sales"] = df["Sales"].clip(lower=0)
df.to_csv(target, index=False)

print("Original rows:", len(pd.read_csv(source)))
print("Cleaned rows:", len(df))
print("Saved:", target)
print(df.head())
