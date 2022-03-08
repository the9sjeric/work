import openpyxl
import pandas as pd
import datetime

"""定义数据函数名"""
sx_fname = "员工岗位职级.xlsx"
mx_fname = "工时明细.xlsx"
cg_fname = "采购、差旅费-模板.xlsx"
jc_fname = "中间数据表(检查用).xlsx"
mb_fname = "目标文件.xlsx"
mb_new_fname = "目标文件(新).xlsx"

wb = openpyxl.load_workbook(f"source/{cg_fname}")
for i in wb.sheetnames:
    ws = wb[i]
    print(ws)
    for image in ws._images:
        print(image)