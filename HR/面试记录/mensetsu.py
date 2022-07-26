import numpy as np
import pandas as pd
import time
import openpyxl
import os
import datetime
from functools import reduce

txt = "填写上周时间.txt"
source = "面试记录表.xlsx"
target = "招聘情况统计表.xlsx"

week = []
f = open(txt, encoding="utf-8")
for i in f.readlines():
    week.append(i.replace("\n", ""))

s_date = datetime.datetime.strptime(week[0], "%Y-%m-%d").date()
e_date = datetime.datetime.strptime(week[1], "%Y-%m-%d").date()
today = datetime.date.today()
# print(today)

df_s = pd.read_excel(source)

df_s1 = df_s[["部门", "岗位", "沟通时间"]].copy()
df_s1 = df_s1[(df_s1["沟通时间"].dt.date >= s_date) & (df_s1["沟通时间"].dt.date <= e_date)]
df_t1 = df_s1.groupby(["部门", "岗位"]).count()
# print(df_t1)

df_s2 = df_s[["部门", "岗位", "专业面时间"]].copy()
df_s2.info()
df_s2["专业面时间"].replace({"/": "1999-09-09"}, inplace=True)
df_s2["专业面时间"] = pd.to_datetime(df_s2["专业面时间"])
df_s2 = df_s2[(df_s2["专业面时间"].dt.date >= s_date) & (df_s2["专业面时间"].dt.date <= e_date)]
df_t2 = df_s2.groupby(["部门", "岗位"]).count()
# print(df_t2)

df_s3 = df_s[["部门", "岗位", "面试结果", "是否发offer", "是否已入职"]].copy()
df_s3.loc[df_s3["面试结果"] != "录用", "面试结果"] = None
df_s3.loc[df_s3["是否发offer"] != "是", "是否发offer"] = None
df_s3.loc[df_s3["是否已入职"] != "是", "是否已入职"] = None
df_t3 = df_s3.groupby(["部门", "岗位"]).count()
# print(df_t3)

df_s4 = df_s[["部门", "岗位", "待入职时间"]].copy()
df_s4["待入职时间"].replace({"/": "1999-09-09"}, inplace=True)
df_s4["待入职时间"] = pd.to_datetime(df_s4["待入职时间"])
df_s4 = df_s4[df_s4["待入职时间"].dt.date >= today]
df_t4 = df_s4.groupby(["部门", "岗位"]).count()
# print(df_t4)

dfs = [df_t1, df_t2, df_t3, df_t4]
df_final = reduce(lambda x, y: pd.merge(x, y, on=["部门", "岗位"], how="outer"), dfs)
df_final = df_final.reset_index()
df_final = df_final.fillna(0)
df_final.rename(columns={'沟通时间': '有效沟通人数', '专业面时间': '面试人数', '面试结果': '录用意向人数',
                         '是否发offer': '发offer数', '是否已入职': '已入职人数', '待入职时间': '待入职人数'},
                inplace=True)
# print(df_final)
df_final.to_excel(target)
