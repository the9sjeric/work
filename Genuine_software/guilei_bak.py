import openpyxl
import pandas as pd
import os
os.chdir(r"C:\Users\jianshen\Desktop\work\098_软件正版化")

excel1 = "Summary_ws.xlsx"
excel2 = "guodu.xlsx"
excel3 = "Summary_ws.xlsx"
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

def df_make(num):
    df = pd.read_excel(excel2,sheet_name=num-1)
    return df

df1 = df_make(1)
df1 = pd.read_excel(excel2,sheet_name=0)
df2 = pd.read_excel(excel2,sheet_name=1)
df3 = pd.read_excel(excel2,sheet_name=2)
df4 = pd.read_excel(excel2,sheet_name=3)
df5 = pd.read_excel(excel2,sheet_name=4)
df6 = pd.read_excel(excel2,sheet_name=5)
df7 = pd.read_excel(excel2,sheet_name=6)
df8 = pd.read_excel(excel2,sheet_name=7)
df9 = pd.read_excel(excel2,sheet_name=8)
df10 = pd.read_excel(excel2,sheet_name=9)
df11 = pd.read_excel(excel2,sheet_name=10)
df12 = pd.read_excel(excel2,sheet_name=11)
df13 = pd.read_excel(excel2,sheet_name=12)
df14 = pd.read_excel(excel2,sheet_name=13)
df15 = pd.read_excel(excel2,sheet_name=14)
df16 = pd.read_excel(excel2,sheet_name=15)
df17 = pd.read_excel(excel2,sheet_name=16)
df18 = pd.read_excel(excel2,sheet_name=17)

df_all = pd.concat(df_list)
df_all = df_all.drop_duplicates()

df_soft_count = df_all.groupby(df_all["软件名称"]).count()

df_pc_count = df_all.groupby(df_all["电脑名称"]).count()

excel3_write = pd.ExcelWriter(excel3)
df_all.to_excel(excel3_write,sheet_name="总表")
df_soft_count.to_excel(excel3_write,sheet_name="soft_count")
df_pc_count.to_excel(excel3_write,sheet_name="PC_count")
excel3_write.close()