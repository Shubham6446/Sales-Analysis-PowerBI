from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
data_file = ROOT / "data" / "cleaned_sales.csv"
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

df = pd.read_csv(data_file, parse_dates=["Order Date"])

print("\nTOTAL SALES:", round(df["Sales"].sum(), 2))
print("\nCATEGORY SALES\n", df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\nREGION SALES\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\nTOP 5 PRODUCTS\n", df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5))

monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
monthly.index = monthly.index.astype(str)
monthly.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(out / "monthly_sales.png")
plt.close()

category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
category.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(out / "category_sales.png")
plt.close()

print("\nCharts saved in outputs/")
