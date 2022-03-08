import pandas as pd
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts

"""定义数据函数名"""
start_data = '面试情况汇总表.xlsx'
end_data = '面试情况汇总_部门别(月度)_数据透视表.xlsx'
end_month_job_html = '面试情况汇总_部门别(月度)_数据透视图.html'

"""定义月份hashmap"""
month_hashmap = {'1': '01月', '2': '02月', '3': '03月', '4': '04月', '5': '05月',
                 '6': '06月', '7': '07月', '8': '08月', '9': '09月', 'A': '10月',
                 'B': '11月', 'C': '12月', '简': '99月'}
"""生成所需数据"""
df = pd.read_excel(start_data)
df_dep = df[['简历编码', '部门', '处理']].copy()
"""处理空值"""
df_dep.fillna(value='简历编码null', inplace=True)
df_dep['部门'].fillna(value='部门null', inplace=True)
df_dep['处理'].fillna(value='处理null', inplace=True)

"""生成<月份>列"""
for number in range(0, len(df_dep)):
    df_dep.loc[number, '月份'] = month_hashmap[str(df_dep.loc[number, '简历编码'])[0]]
"""生成数据透视表"""
res = pd.pivot_table(df_dep, index=['月份', '部门'], columns=['处理'],
                         aggfunc=len, margins=True)
"""生成月份数据"""
month = []
for menber in res.index:
    if menber[0] not in month:
        month.append(menber[0])
"""建立轮播图"""
tl = Timeline()
for tsuki in month:
    month_data = res.loc[tsuki]
    bar = Bar()
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title=f'面试情况汇总_{tsuki}', pos_left='40%'),
        legend_opts=opts.LegendOpts(pos_top='5%'))
    bar.add_xaxis(xaxis_data=month_data.index.tolist())

    for num in range(0, len(month_data.columns)):
        bar.add_yaxis(series_name=month_data.columns[num][1],
                      y_axis=month_data[month_data.columns[num]].tolist())

    tl.add(chart=bar, time_point=tsuki)
tl.render('888.html')