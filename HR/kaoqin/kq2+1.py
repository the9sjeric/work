import pandas as pd

source1 = "hik.xlsx"
source2 = "dingding.xlsx"
target = "考勤(2合1结果).xlsx"

"""选取源文件所需列"""
df_source1 = pd.read_excel(source1)
df_target1 = df_source1[["人员姓名", "工号", "事件时间"]].copy()
df_target1 = df_target1.fillna("空值")

"""创建表示“年月日”的日期列(hik)"""
df_target1.insert(2, "日期", df_target1["事件时间"])
df_target1["日期"] = pd.to_datetime(df_target1["日期"])
df_target1["日期"] = df_target1["日期"].dt.strftime("%Y-%m-%d")
df_target1["事件时间"] = pd.to_datetime(df_target1["事件时间"])

"""创建表示“年月日”的日期列(dingding)"""
df_source2 = pd.read_excel(source2)
df_target2 = df_source2[["姓名", "工号", "日期", "打卡时间"]].copy()
df_target2 = df_target2.fillna("空值")
df_target2["666"] = df_target2["日期"].dt.strftime("%Y-%m-%d")
df_target2["日期"] = df_target2["日期"].dt.date
df_target2["打卡时间"] = df_target2["666"].map(str) + " " + df_target2["打卡时间"].map(str)
df_target2["打卡时间"] = pd.to_datetime(df_target2["打卡时间"])
df_target2 = df_target2.drop(labels="666", axis=1)
df_target2.rename(columns={'姓名': '人员姓名', '打卡时间': '事件时间'}, inplace=True)


"""合并hik和dingding"""
df_target1 = pd.concat([df_target1, df_target2])
df_target1.to_excel("数据合并表(检查用).xlsx")

"""计算每天最早和最晚的打卡时间"""
df_1 = df_target1.groupby(["人员姓名", "工号", "日期"])
df_2 = df_1["事件时间"]
df_3 = df_2.agg([("上班打卡", "min"), ("下班打卡", "max")])
df_4 = df_3.reset_index()

"""创建表示“周几”的星期列"""
df_4.insert(2, "星期", df_4["日期"])
df_4["星期"] = pd.to_datetime(df_4["星期"])
df_4["星期"] = df_4["星期"].dt.dayofweek + 1


"""计算一天的工作时长"""
df_4["工作时长"] = ""
for i in range(0, len(df_4)):
    df_4.loc[i, "工作时长"] = round((df_4.loc[i, "下班打卡"] - df_4.loc[i, "上班打卡"]).seconds / 3600, 1)

"""计算上班考勤（上午迟到、上午旷工、下午迟到、全天旷工）"""
df_4["上班考勤情况"] = ""
df_4["迟到/旷工\n(小时)"] = ""
df_4["迟到/旷工\n(分钟)"] = ""
for i in range(0, len(df_4)):
    amsbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 09:00:00")
    amwdsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 09:15:00")
    amcdsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 11:00:00")
    amxbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 12:00:00")
    pmsbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 13:00:00")
    pmcdsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 14:00:00")
    pmxbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 18:00:00")
    if df_4.loc[i, "星期"] in [6, 7]:
        df_4.loc[i, "上班考勤情况"] = "周末加班"
    else:
        if df_4.loc[i, "上班打卡"] <= amsbsj:
            df_4.loc[i, "上班考勤情况"] = ""
        elif amsbsj < df_4.loc[i, "上班打卡"] <= amwdsj:
            df_4.loc[i, "上班考勤情况"] = "上午晚到"
            df_4.loc[i, "迟到/旷工\n(小时)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 3600, 1)
            df_4.loc[i, "迟到/旷工\n(分钟)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 60, 1)
        elif amwdsj < df_4.loc[i, "上班打卡"] <= amcdsj:
            df_4.loc[i, "上班考勤情况"] = "上午迟到"
            df_4.loc[i, "迟到/旷工\n(小时)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 3600, 1)
            df_4.loc[i, "迟到/旷工\n(分钟)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 60, 1)
        elif amcdsj < df_4.loc[i, "上班打卡"] <= amxbsj:
            df_4.loc[i, "上班考勤情况"] = "上午旷工"
            df_4.loc[i, "迟到/旷工\n(小时)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 3600, 1)
            df_4.loc[i, "迟到/旷工\n(分钟)"] = round((df_4.loc[i, "上班打卡"] - amsbsj).seconds / 60, 1)
        elif amxbsj < df_4.loc[i, "上班打卡"] <= pmsbsj:
            df_4.loc[i, "上班考勤情况"] = "上午旷工"
            df_4.loc[i, "迟到/旷工\n(小时)"] = 3.0
            df_4.loc[i, "迟到/旷工\n(分钟)"] = 180.0
        elif pmsbsj < df_4.loc[i, "上班打卡"] <= pmcdsj:
            df_4.loc[i, "上班考勤情况"] = "上午旷工，下午迟到"
            df_4.loc[i, "迟到/旷工\n(小时)"] = round((df_4.loc[i, "上班打卡"] - pmsbsj).seconds / 3600, 1) + 3.0
            df_4.loc[i, "迟到/旷工\n(分钟)"] = round((df_4.loc[i, "上班打卡"] - pmsbsj).seconds / 60, 1) + 180.0
        elif pmcdsj < df_4.loc[i, "上班打卡"] <= pmxbsj:
            df_4.loc[i, "上班考勤情况"] = "全天旷工"
            df_4.loc[i, "迟到/旷工\n(小时)"] = round((df_4.loc[i, "上班打卡"] - pmsbsj).seconds / 3600, 1) + 3.0
            df_4.loc[i, "迟到/旷工\n(分钟)"] = round((df_4.loc[i, "上班打卡"] - pmsbsj).seconds / 60, 1) + 180.0
        else:
            df_4.loc[i, "上班考勤情况"] = "上班打卡时间晚于规定下班时间，请检查"

"""计算下班考勤（早退）"""
df_4["下班考勤情况"] = ""
df_4["早退/旷工\n(小时)"] = ""
df_4["早退/旷工\n(分钟)"] = ""
for i in range(0, len(df_4)):
    pmxbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 18:00:00")
    pmztsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 17:00:00")
    pmkgsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 14:00:00")
    pmsbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 13:00:00")
    amsbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 09:00:00")
    amwdsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 09:30:00")
    amxbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 12:00:00")
    if df_4.loc[i, "星期"] in [6, 7]:
        df_4.loc[i, "下班考勤情况"] = "周末加班"
    else:
        if df_4.loc[i, "下班打卡"] >= pmxbsj:
            df_4.loc[i, "下班考勤情况"] = ""
        elif pmxbsj > df_4.loc[i, "下班打卡"] >= pmztsj:
            df_4.loc[i, "下班考勤情况"] = "早退"
            df_4.loc[i, "早退/旷工\n(小时)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 3600, 1)
            df_4.loc[i, "早退/旷工\n(分钟)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 60, 1)
        elif pmztsj > df_4.loc[i, "下班打卡"] >= pmkgsj:
            df_4.loc[i, "下班考勤情况"] = "下午旷工"
            df_4.loc[i, "早退/旷工\n(小时)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 3600, 1)
            df_4.loc[i, "早退/旷工\n(分钟)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 60, 1)
        elif pmkgsj > df_4.loc[i, "下班打卡"] >= pmsbsj:
            df_4.loc[i, "下班考勤情况"] = "全天旷工"
            df_4.loc[i, "早退/旷工\n(小时)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 3600, 1)
            df_4.loc[i, "早退/旷工\n(分钟)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 60, 1)
        elif pmsbsj > df_4.loc[i, "下班打卡"] >= amxbsj:
            df_4.loc[i, "下班考勤情况"] = "全天旷工"
            df_4.loc[i, "早退/旷工\n(小时)"] = 5.0
            df_4.loc[i, "早退/旷工\n(分钟)"] = 300.0
        elif amxbsj > df_4.loc[i, "下班打卡"] > amsbsj:
            df_4.loc[i, "下班考勤情况"] = "全天旷工"
            df_4.loc[i, "早退/旷工\n(小时)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 3600, 1) - 1.0
            df_4.loc[i, "早退/旷工\n(分钟)"] = round((pmxbsj - df_4.loc[i, "下班打卡"]).seconds / 60, 1) - 60.0
        else:
            df_4.loc[i, "下班考勤情况"] = "下班打卡时间早于规定上班时间，请检查"

"""计算加班时间"""
df_4["加班考勤"] = ""
df_4["加班小时"] = ""
df_4["加班分钟"] = ""
for i in range(0, len(df_4)):
    pmxbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 18:00:00")
    jbsj = pd.to_datetime(f"{df_4.loc[i, '日期']} 19:50:00")
    if df_4.loc[i, "星期"] in [6, 7]:
        df_4.loc[i, "加班考勤"] = "周末加班"
        df_4.loc[i, "加班小时"] = round((df_4.loc[i, "下班打卡"] - df_4.loc[i, "上班打卡"]).seconds / 3600, 1)
        df_4.loc[i, "加班分钟"] = round((df_4.loc[i, "下班打卡"] - df_4.loc[i, "上班打卡"]).seconds / 60, 1)
    else:
        if df_4.loc[i, "下班打卡"] >= jbsj:
            df_4.loc[i, "下班考勤情况"] = "平日加班"
            df_4.loc[i, "加班考勤"] = "平日加班"
            df_4.loc[i, "加班小时"] = round((df_4.loc[i, "下班打卡"] - pmxbsj).seconds / 3600, 1)
            df_4.loc[i, "加班分钟"] = round((df_4.loc[i, "下班打卡"] - pmxbsj).seconds / 60, 1)

"""简化上下班打卡时间格式"""
df_4["上班打卡"] = df_4["上班打卡"].dt.strftime("%H:%M:%S")
df_4["下班打卡"] = df_4["下班打卡"].dt.strftime("%H:%M:%S")
df_4.to_excel(target)