import pandas as pd
from pyecharts.charts import Timeline, Bar
from pyecharts import options as opts

"""定义数据函数名"""
start_data = '面试情况汇总表.xlsx'
end_data = '面试情况汇总(月度)_数据透视表.xlsx'
end_month_job_html = f'面试情况汇总(月度)_数据透视图.html'

'''月份hashmap'''
month_hashmap = {'1': '01月', '2': '02月', '3': '03月', '4': '04月', '5': '05月',
                 '6': '06月', '7': '07月', '8': '08月', '9': '09月', 'A': '10月',
                 'B': '11月', 'C': '12月', '简': '99月'}
"""读取数据源"""
df = pd.read_excel(start_data)
'''<简历编码>填充空白值'''
df['简历编码'].fillna('简历编码_null', inplace=True)
'''增加月份相关数据'''
for i in range(0, len(df)):
    df.loc[i, '月份'] = month_hashmap[str(df.loc[i, '简历编码'])[0]]

"""简化数据，仅提取所需数据"""
df_month_job = df[['月份', '部门', '招聘岗位', '处理']].copy()
"""填充空白值”"""
df_month_job['处理'].fillna('处理方式_null', inplace=True)
df_month_job['部门'].fillna('部门_null', inplace=True)
df_month_job['招聘岗位'].fillna('招聘岗位_null', inplace=True)
"""生成数据透视表"""
res = pd.pivot_table(df_month_job.copy(), index=['月份'], values=['处理'],
                     columns=['招聘岗位'], aggfunc=len, margins=True)
"""保存数据透视表"""
res.to_excel(end_data)

# print(res.loc['08月'].loc['上位机'].loc['产品BU'])


# """""""""""""<制作数据透视-轮播图>"""""""""""""
# """实例化轮播图&柱状图"""
# tl = Timeline(init_opts=opts.InitOpts(width='1100px', height='550px'))
# tl.add_schema(orient='vertical', pos_right='3%', height='500px',
#               width='50px', is_inverse=True)
# bar = Bar()
#
# """制作月度name列表"""
# month_name_all = []
# for i in res.index:
#     if i[0] not in month_name_all:
#         month_name_all.append(i[0])
#
# """制作岗位&月度相关数据透视"""
# res_month_job = pd.pivot_table(df_month_job.copy(), index=['月份', '招聘岗位'],
#                                values=['处理'], columns=["部门"], aggfunc=len, margins=True)
# """循环制作柱状图并添加到轮播图中"""
# for time_node in month_name_all:
#     res_need_month = res_month_job.copy().loc[time_node]
#     """将空值填充为“0”"""
#     res_need_month.fillna(inplace=True, value=0)
#     """实例化柱形图"""
#     bar = Bar()
#     """添加柱形图标题"""
#     bar.set_global_opts(
#         title_opts=opts.TitleOpts(title=f"面试情况汇总({time_node})", pos_left='35%'),
#         legend_opts=opts.LegendOpts(pos_top='5%'),
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
#         yaxis_opts=opts.AxisOpts(max_=max(res_need_month['部门']['All'].tolist()) + 5))
#     """添加柱形图横坐标"""
#     bar.add_xaxis(xaxis_data=res_need_month.index.tolist())
#     """添加柱形图纵坐标"""
#     for i in range(0, len(res_need_month.columns)):
#         bar.add_yaxis(
#             series_name=res_need_month.columns[i][1],
#             y_axis=res_need_month[res_need_month.columns[i]].tolist())
#     """将柱状图添加到轮播图中"""
#     tl.add(chart=bar, time_point=time_node)
#
# """保存最终的轮播图"""
# tl.render(end_month_job_html)