# 使用import导入openpyxl模块
import openpyxl
# 使用from...import从pyecharts.charts
# 导入Timeline模块和Bar模块
from pyecharts.charts import Timeline, Bar
# 使用from...import从pyecharts导入options模块，简写为opts
from pyecharts import options as opts

# 将文件路径 023_lunbotu.xlsx 赋值给path
path = "023_lunbotu.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用wb[]读取工作表GDP，赋值给sheet
sheet = wb["GDP"]


# 定义函数get_data()传入参数row(行数)
def get_data(row):
    # 新建列表countryList存储国家
    countryList = []
    # 新建列表numberList存储GDP
    numberList = []

    # for循环配合range()遍历1到10
    for index in range(1, 11):
        # 使用 sheet[] 读取第row行的数据赋值给countryRow
        countryRow = sheet[row]
        # 使用 sheet[] 读取第row+1行的数据赋值给numberRow
        numberRow = sheet[row + 1]
        # 使用append()函数
        # 将countryRow单元格的值添加进列表countryList
        countryList.append(countryRow[index].value)
        # 使用append()函数
        # 将numberRow单元格的值添加进列表numberList
        numberList.append(numberRow[index].value)
    # 将每行的第一个元素，年份赋值给year
    year = countryRow[0].value
    # 使用return返回(year, countryList, numberList)
    return (year, countryList, numberList)


# TODO 使用Timeline创建对象赋值给tl
tl = Timeline()

# 使用for循环遍历列表[2,4,6,8,10,12,14,16,18,20]
for num in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
    # TODO 调用get_data()函数，将参数num传入，赋值给data
    data = get_data(num)

    # 使用Bar()函数创建对象赋值给变量bar
    bar = Bar()

    # TODO 添加参数xaxis_data=data[1]，传入add_xaxis()函数
    bar.add_xaxis(xaxis_data=data[1])

    # TODO 将series_name设置为空，data[2]赋值给y_axis，传入add_yaxis()函数
    bar.add_yaxis(series_name="", y_axis=data[2])

    # 使用全局配置项，将标题设置为x年前十大经济体GDP排名
    bar.set_global_opts(title_opts=opts.TitleOpts(title=f"{data[0]}年前十大经济体GDP排名"))

    # TODO 将bar赋值给chart，以格式化将f"{data[0]}年"赋值给time_point
    # 使用add()函数依次传入参数
    tl.add(chart=bar, time_point=f"{data[0]}年")

# 使用render()生成文件保存到/Users/GDP.html
tl.render("轮播图.html")