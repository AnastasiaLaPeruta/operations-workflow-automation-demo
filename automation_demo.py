
import pandas as pd

df = pd.read_csv("messy_intake_data.csv")

df["client_name"] = df["client_name"].str.strip().str.title()
df["email"] = df["email"].str.strip().str.lower()
df["status"] = df["status"].str.strip().str.lower()

df = df.drop_duplicates(subset=["email"])

summary = df.groupby("status")["revenue"].sum().reset_index()

df.to_csv("cleaned_data.csv", index=False)
summary.to_csv("revenue_summary.csv", index=False)

print("Automation completed.")
