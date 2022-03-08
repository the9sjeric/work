import pandas as pd

file_name = "ipguard_source/杭州电脑_ipguard安装清单(固定资产版).xlsx"

wb = pd.read_excel(file_name)
wb01 = wb.groupby("使用人").count()
print(wb01)
wb01.to_excel("duibi.xlsx")