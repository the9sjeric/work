import pandas as pd

project_list = []
df_project = pd.read_excel("..\项目编码.xls")
for i in range(0, len(df_project)):
    project_list.append(df_project.loc[i,"项目编号"])
