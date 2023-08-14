import pandas as pd


df = pd.read_csv("data/[your data file].csv")

df = df.drop(labels = ["columns to be dropped"], axis=1)

df.to_csv("data/[your data file].csv", index=False)
