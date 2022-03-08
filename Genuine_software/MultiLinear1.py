import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

#排潮风门开度 K
K1 = -0.056604787685608
# 薄板后温度 K
K2 = -0.122090006359242
df = pd.read_csv('processed_data_50.csv')
new_data = df[['时间', '排潮风门实际开度', '薄板后温度', '热风机频率', '入口水分', '出口水分']]
# print(new_data.head(5))
new_data.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'y']
# print(new_data.head(5))
new_data.x2 = new_data.x2 * K1
new_data.x3 = new_data.x3 * K2
# print(new_data.head(5))
print(new_data)
from statsmodels.formula.api import ols
# 小写的 ols 函数才会自带截距项，OLS 则不会
# 固定格式：因变量 ~ 自变量(+ 号连接)
lm = ols('y ~ x1 + x2 + x3 + x4 + x5', data = new_data).fit()





