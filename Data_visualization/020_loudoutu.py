# 使用from...import从pyecharts.charts导入Funnel
from pyecharts.charts import Funnel
# 使用from...import从pyecharts导入options，简写为opts
from pyecharts import options as opts

# 存储用户行为的列表user_behavior
user_behavior = ["浏览商品","加入购物车","生成订单","支付订单","完成交易"]
# 存储各环节用户数量的列表num
num = [100, 40, 30, 20, 17]

# 定义一个列表用于存储新的数据total
total = []
# 使用for循环遍历0～4
for i in range(0, 5):
    # TODO 新建列表temp
    temp = []
    # TODO 使用if判断i等于0时
    if i == 0 :
        # TODO 使用append()将user_behavior[i]和100%追加到列表temp
        temp.append(user_behavior[i]+"100%")
    # TODO 否则
    else:
        # TODO 使用(当前项/前一项)*100，赋值给pass_rate
        pass_rate = (num[i]/num[i-1])*100
        # TODO 使用round()保留pass_rate的一位小数，赋值给percent
        percent = round(pass_rate,1)
        # TODO 使用append()将标签和格式化组成的x%追加到列表temp
        temp.append(user_behavior[i]+f"{percent}%")
    # TODO 使用append()将num[i]追加到列表temp
    temp.append(num[i])
    # TODO 使用append()将temp追加到列表total
    total.append(temp)

# TODO 使用Funnel()函数创建实例赋值给funnel
funnel = Funnel()

# TODO 将series_name设为空，将total赋值给data_pair，设置gap值为10
# 将参数添加到add()函数中
funnel.add(series_name="",data_pair=total,gap=10)

# 使用LegendOpts()，传入参数is_show=False，赋值给legend_opts，隐藏图例
# 使用TitleOpts()，设置标题为"用户行为转化率"，赋值给title_opts
funnel.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False),
    title_opts=opts.TitleOpts(title="用户行为转化率"))

# 使用render()生成漏斗图，存到路径/Users/user_conversion_rate.html
funnel.render("漏斗图.html")