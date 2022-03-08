import pandas as pd
import numpy as np
df = pd.read_excel("数据汇总表(初稿).xlsx")

df01 = df[["类别", "项目编号", "金额"]]

data_frame = pd.pivot_table(df01,index=["项目编号"],columns=["类别"],aggfunc=np.sum,margins=True)
print(data_frame)
