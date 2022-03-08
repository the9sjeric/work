import openpyxl

import os
dir_path = r"D:\998_GS_Statistics\001_Summary_list"
os.chdir(dir_path)
file_list = os.listdir(dir_path)

file_name_list = []
for file in file_list:
    file_name = os.path.splitext(file)[0]
    file_name_list.append(file_name)

wb = openpyxl.Workbook()

for item in file_name_list:
    file_full_name = item + ".txt"
    fopen = open(file_full_name, "r")
    lines = fopen.readlines()
    ws_new = wb.create_sheet(item)
    a = 0
    for line in lines:
        a = a + 1
        ws_new[f"A{a}"].value = line

wb.save(r"D:\998_GS_Statistics\Summary_ws.xlsx")

