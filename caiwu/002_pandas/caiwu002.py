import pandas as pd
import numpy as np
import re

start_file = "序时账.xls"
end_file = "汇总表.xlsx"

chai_lv_fei = ["差旅费", "市内交通费"]
ye_wu_fei = ["业务费"]
ren_gong_fei = ["工资奖金", "职工社保", "职工公积金", "职工福利费"]

project_list = ["期初余额", "小计"]

df = pd.read_excel(start_file)
df["项目编码"] = ""

# 匹配项目相关行，并在项目编码列追加标记
for i in range(0, len(df)):
    res_find = re.search(r'[a-zA-Z]{2,6}[0-9]{4,9}', str(df.loc[i, "摘要"]))
    if df.loc[i, "摘要"] in project_list:
        df.loc[i, "项目编码"] = df.loc[i, "摘要"]
    elif res_find:
        df.loc[i, "项目编码"] = res_find.group(0)

# 匹配科目
df["科目"] = ""
for i in range(0,len(df)):
    if df.loc[i, "科目名称"] in chai_lv_fei:
        df.loc[i,"科目"] = "差旅费"
    elif df.loc[i, "科目名称"] in ye_wu_fei:
        df.loc[i, "科目"] = "业务费"
    elif df.loc[i, "科目名称"] in ren_gong_fei:
        df.loc[i, "科目"] = "人工费"
    elif pd.isnull(df.loc[i, "科目名称"]):
        df.loc[i, "科目"] = None
    else:
        df.loc[i, "科目"] = "其他"

df.to_excel(end_file)
###########################################
df_DP = df[["科目", "项目编码", "金额"]]
res = pd.pivot_table(df_DP, index=["项目编码"], columns=["科目"], aggfunc=np.sum, margins=True)
res.to_excel("数据透视表.xlsx")
