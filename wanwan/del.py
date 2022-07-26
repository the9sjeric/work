import pandas as pd

source = "data.xlsx"
target = "结果.xlsx"

"""选取源文件所需列"""
df_source = pd.read_excel(source)
print(df_source)
aaa = []
for i in range(51, 61):
    aaa.append(i)
for i in range(81, 91):
    aaa.append(i)

df_source = df_source.drop(aaa)

df_source.to_excel(target)