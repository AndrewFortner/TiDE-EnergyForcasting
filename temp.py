# read in datasets/electricity/PJME_daily_sorted.csv, drop the 'doy' column, and save as datasets/electricity/PJME_daily_sorted_OT_only.csv
import pandas as pd
df = pd.read_csv("datasets/electricity/PJME_daily_sorted.csv")
df = df.drop(columns=['doy'])
df.to_csv("datasets/electricity/PJME_daily_sorted_OT_only.csv", index=False)

