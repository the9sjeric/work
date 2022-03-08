import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

"""定义数据函数名"""
start_data = '面试情况汇总表.xlsx'
end_data = '面试情况汇总(月度)_数据透视表.xlsx'
month = '七月'
end_month_html = f'面试情况汇总({month})_数据透视图.html'

'''月份hashmap'''
month_hashmap = {'1': '一月', '2': '二月', '3': '三月', '4': '四月', '5': '五月', '6': '六月',
                 '7': '七月', '8': '八月', '9': '九月', 'A': '十月', 'B': '11月', 'C': '十二月',
                 '简': '月份_null'}
"""读取数据源"""
df = pd.read_excel(start_data)
'''<简历编码>填充空白值'''
df['简历编码'].fillna('简历编码_null', inplace=True)
'''增加月份相关数据'''
for i in range(0, len(df)):
    df.loc[i, '月份'] = month_hashmap[str(df.loc[i, '简历编码'])[0]]


"""简化数据，仅提取所需数据"""
df_zhengli = df[['月份', '部门', '招聘岗位', '处理']]
"""填充空白值”"""
df_zhengli['处理'].fillna('处理方式_null', inplace=True)
df_zhengli['部门'].fillna('部门_null', inplace=True)
df_zhengli['招聘岗位'].fillna('招聘岗位_null', inplace=True)
"""生成数据透视表"""
res = pd.pivot_table(df_zhengli, index=['月份', '部门', '招聘岗位'], columns=["处理"],
                     aggfunc=len, margins=True)
"""保存数据透视表"""
res.to_excel(end_data)



"""制作数据透视图"""
res_month_gangwei = pd.pivot_table(df_zhengli, index=['月份', '招聘岗位'], columns=["处理"],
                     aggfunc=len, margins=True)
res_need_month = res_month_gangwei.loc[month]
"""将空值填充为“0”"""
res_need_month.fillna(value=0, inplace=True)
"""实例化柱形图"""
bar = Bar()
"""添加柱形图标题"""
bar.set_global_opts(title_opts=opts.TitleOpts(title=f"面试情况汇总({month})_数据透视图"),
                    legend_opts=opts.LegendOpts(pos_top='10%'))
"""添加柱形图横坐标"""
bar.add_xaxis(xaxis_data=res_need_month.index.tolist())
"""添加柱形图纵坐标"""
for i in range(0, len(res_need_month.columns)):
    bar.add_yaxis(series_name=res_need_month.columns[i][1],
                  y_axis=res_need_month[res_need_month.columns[i]].tolist())
bar.render(end_month_html)