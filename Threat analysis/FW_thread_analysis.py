import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Bar

plt.rcParams["font.sans-serif"] = ["SimHei"]
df = pd.read_csv("Threat log.csv")

df["时间"] = pd.to_datetime(df["时间"])
df = df.set_index("时间")
df_time = df.groupby("攻击者").count()
# print(df_time)
# plt.bar(df_time.index,df_time["受害者"])
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

print(df_time.index)
bar = Bar()
bar.add_xaxis(xaxis_data=df_time.index)
bar.add_yaxis(series_name="攻击者地图",y_axis=df_time["受害者"])
bar.render("bar.html")