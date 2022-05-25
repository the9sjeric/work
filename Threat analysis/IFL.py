import pandas as pd

data = pd.read_csv("bilibili.csv")

df = data.groupby("author").count()
count = df["分区"].reset_index()
count.columns = ["author", "times"]
com = pd.merge(count, data, on="author", how="inner")
com["date"] = pd.to_datetime(com["date"])
result = com[com["times"] >= 5]

I = (result.groupby(result["author"])["danmu"].sum() + result.groupby(result["author"])["reply"].sum()) \
    / result.groupby(result["author"])["view"].sum() / result.groupby(result["author"])["danmu"].count() * 100

F = (result.groupby(result["author"])["date"].max() - result.groupby(result["author"])["date"].min()).dt.days \
    / result.groupby(result["author"])["danmu"].count()

L = (result.groupby(result["author"])["likes"].sum() + result.groupby(result["author"])["coins"].sum() + result.groupby(result["author"])["favorite"].sum()) \
    / result.groupby(result["author"])["view"].sum() * 100

IFL = pd.concat([I, F, L], axis=1)
IFL.columns = ["I", "F", "L"]
IFL["I_score"] = pd.qcut(IFL["I"], q=5, labels=[1, 2, 3, 4, 5])
IFL["F_score"] = pd.qcut(IFL["F"], q=5, labels=[5, 4, 3, 2, 1])
IFL["L_score"] = pd.qcut(IFL["L"], q=5, labels=[1, 2, 3, 4, 5])
def biaoji(item):
    if item > 3:
        return 1
    else:
        return 0
IFL["I_score"] = IFL["I_score"].apply(biaoji)
IFL["F_score"] = IFL["F_score"].apply(biaoji)
IFL["L_score"] = IFL["L_score"].apply(biaoji)
IFL["mark"] = IFL["I_score"].astype(str) + IFL["F_score"].astype(str) + IFL["L_score"].astype(str)

def zhuanhua(item):
    if item == "111":
        return "高质量UP主"
    elif item == "101":
        return "高质量拖更UP主"
    elif item == "011":
        return "高质量内容高深UP主"
    elif item == "001":
        return "高质量内容高深拖更UP主"
    elif item == "110":
        return "接地气活跃UP主"
    elif item == "100":
        return "接地气UP主"
    elif item == "010":
        return "活跃UP主"
    elif item == "000":
        return "还在成长的UP主"
IFL["up_type"] = IFL["mark"].apply(zhuanhua)
zuihou = IFL["up_type"].groupby(IFL["up_type"]).count() / IFL["up_type"].groupby(IFL["up_type"]).count().sum()

import matplotlib.pyplot as plt

# plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.rcParams["font.sans-serif"] = "SimHei"
plt.bar(zuihou.index, zuihou.values)
plt.xticks(rotation=45)

plt.show()