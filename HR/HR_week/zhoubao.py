import numpy as np
import pandas as pd

hashmap = {'优化控制': '算法工程师（优化控制）', '视觉算法': '算法工程师（视觉方向）', '数据治理': '数据治理工程师',
           '软件后端': '软件后端开发', '上位机': '上位机开发工程师', 'All': '小计'}

df = pd.read_excel("面试情况汇总表模板.xlsx")
muban = pd.read_excel("招聘周报-模板.xlsx")

df_zhengli = df[['部门', '招聘岗位', '处理']]
df_zhengli['处理'].fillna('空白填充', inplace=True)

res = pd.pivot_table(df_zhengli, index=["招聘岗位"], columns=["处理"], aggfunc=np.count_nonzero, margins=True)
res.to_excel('数据透视.xlsx')
