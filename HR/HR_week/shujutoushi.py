import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

"""定义数据函数名"""
start_data = '面试情况汇总表模板.xlsx'
end_data = '面试情况汇总_数据透视表.xlsx'
end_html = '面试情况汇总_数据透视图.html'

"""读取数据源"""
df = pd.read_excel(start_data)
"""简化数据，仅提取所需数据"""
df_zhengli = df[['部门', '招聘岗位', '处理']]
"""将空值填充为“空白填充”"""
df_zhengli['处理'].fillna('空白填充', inplace=True)
"""生成数据透视表"""
res = pd.pivot_table(df_zhengli, index=["招聘岗位"], columns=["处理"], aggfunc=np.count_nonzero, margins=True)
"""保存数据透视表"""
res.to_excel(end_data)

print(res)
"""制作数据透视图"""
"""将空值填充为“0”"""
res.fillna(value=0,inplace=True)
"""实例化柱形图"""
bar = Bar()
"""添加柱形图标题"""
bar.set_global_opts(title_opts=opts.TitleOpts(title="面试情况汇总_数据透视图"),
                    legend_opts=opts.LegendOpts(pos_top='10%'))
"""添加柱形图横坐标"""
bar.add_xaxis(xaxis_data=res.index.tolist())
"""添加柱形图纵坐标"""
for i in range(0, len(res.columns)):
    bar.add_yaxis(series_name=res.columns[i][1], y_axis=res[res.columns[i]].tolist())

bar.render('面试情况汇总_数据透视图.html')