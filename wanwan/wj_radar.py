from pyecharts.charts import Radar
from pyecharts import options as opts

radar = Radar()
c_schema = [
    {"name": "身高", "max": 190, "min": 140},
    {"name": "体重", "max": 100, "min": 0},
    {"name": "学历", "max": 4, "min": 1},
    {"name": "知识储备", "max": 100, "min": 0},
    {"name": "能力", "max": 100, "min": 0},
    {"name": "情商", "max": 100, "min": 0}
]
wenjun = [[170, 60, 1, 60, 70, 85]]

radar.add_schema(schema=c_schema)
radar.add("文军属性图", wenjun, color="#800080",areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
radar.set_global_opts()
radar.render("文军属性图.html")