"""Create the 80/20 working/reporting split. Run once; do not re-run.

The reporting set (Data/reporting_set.csv) is held out and must stay
untouched until the project's final phase.
"""
import pandas as pd
from sklearn.model_selection import train_test_split

RAW = "Data/raw/WHR26_Data_Figure_2.1.xlsx"
SEED = 42

df = pd.read_excel(RAW)
working, reporting = train_test_split(
    df, test_size=0.20, random_state=SEED, stratify=df["Year"]
)
working.sort_index().to_csv("Data/working_set.csv", index=False)
reporting.sort_index().to_csv("Data/reporting_set.csv", index=False)
print(f"total={len(df)} working={len(working)} reporting={len(reporting)}")
