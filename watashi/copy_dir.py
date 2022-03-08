import os
import shutil

muban = "./muban"
path = "./文件夹拷贝/6666"
copypath = "./8888"
allItems = os.listdir(path)

print(allItems)
for i in allItems:
    shutil.copytree(f"{path}/{i}", f"{copypath}/{i}")