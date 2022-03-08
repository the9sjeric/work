import openpyxl
import pandas as pd
import os
os.chdir(r"D:\998_GS_Statistics")

excel1 = "Summary_ws.xlsx"
excel2 = "guodu.xlsx"
excel3 = "Summary_wb.xlsx"
wb = openpyxl.load_workbook(excel1)

for sheet in wb.worksheets:
    b = 1
    for row in sheet.rows:
        if row[0].value != None:
            sheet[f"B{b}"].value = sheet.title
            b = b + 1
    sheet.insert_rows(0)
    sheet["A1"].value = "软件名称"
    sheet["B1"].value = "电脑名称"
wb.save(excel2)

df_list = []
def df_make(num):
    df = pd.read_excel(excel2,sheet_name=num-1)
    return df
for i in range(1,56):
    df_list.append(df_make(i))

df_all = pd.concat(df_list)
df_all = df_all.drop_duplicates()

df_soft_count = df_all.groupby(df_all["软件名称"]).count()

df_pc_count = df_all.groupby(df_all["电脑名称"]).count()

excel3_write = pd.ExcelWriter(excel3)
df_all.to_excel(excel3_write,sheet_name="总表")
df_soft_count.to_excel(excel3_write,sheet_name="soft_count")
df_pc_count.to_excel(excel3_write,sheet_name="PC_count")
excel3_write.close()