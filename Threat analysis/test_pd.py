import pandas as pd

df = pd.read_csv("bilibili.csv")
print(df.loc[df.index[:5]])