import pandas as pd
import numpy as np
from scipy.stats import zscore

df1 = pd.read_csv("ryde_poi_summary.csv")

df2 = pd.read_csv("Inner_West_poi_summary (1).csv")

df3 = pd.read_csv("Parramatta_poi_summary (2).csv")

df4 = pd.read_csv("Sutherland_poi_summary (1).csv")

df = pd.concat([df1, df2, df3, df4], ignore_index=True)

df["z_score"] = zscore(df["poi_count"])

df["score"] = 1 / (1 + np.exp(-df["z_score"]))

print(df)

df.to_csv("all_sa4_scores.csv", index=False)

print("Task 3 scoring saved")