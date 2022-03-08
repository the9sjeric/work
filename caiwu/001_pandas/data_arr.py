import pandas as pd
import re
# 定义文件名变量
start_file = "预付账款.xls"
end_file = "项目预付款.xlsx"
# 通过导出的项目编码文件建立项目编号列表project_list
project_list = ["期初余额", "小计"]

# 读取原始数据，在最后插入备注列
df = pd.read_excel(start_file)
df["备注"] = ""

# 匹配项目相关行，并在备注列追加标记
for i in range(0, len(df)):
    res_find = re.search(r'[a-zA-Z]{2,6}[0-9]{4,9}', df.loc[i, "摘要"])
    if df.loc[i, "摘要"] in project_list:
        df.loc[i, "备注"] = df.loc[i, "摘要"]
    elif res_find:
        df.loc[i, "备注"] = res_find.group(0)

# 筛选小计为平的公司，并在备注列追加标记
ping_list = []
for i in range(0,len(df)):
    if df.loc[i, "摘要"] == "小计" and df.loc[i, "方向"] == "平" :
        ping_list.append(df.loc[i,"供应商名称"])
for i in range(0,len(df)):
    if df.loc[i, "供应商名称"] in ping_list:
        df.loc[i, "备注"] = "平"

# 保存的最后处理过的数据
df.to_excel(end_file)