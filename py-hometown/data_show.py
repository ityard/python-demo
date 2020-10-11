import json, pandas as pd
from collections import Counter
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType

df = pd.read_csv("comments.csv")

# 评分星级
rates = []
for s in df.iloc[:, 3]:
    rates.append(s)
sx = ["五星", "四星", "三星", "二星", "一星"]
sy = [
    str(rates.count(5.0) + rates.count(4.5)),
    str(rates.count(4.0) + rates.count(3.5)),
    str(rates.count(3.0) + rates.count(2.5)),
    str(rates.count(2.0) + rates.count(1.5)),
    str(rates.count(1.0) + rates.count(0.5))
]
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='700px', height='400px'))
    .add("", list(zip(sx, sy)), radius=["40%", "70%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="评分星级比例", subtitle="数据来源：猫眼电影", pos_left = "left"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render_notebook()

# 性别比例
rates = []
for s in df.iloc[:, 8]:
    if s != 1 and s != 2:
        s = 3
    rates.append(s)
gx = ["男", "女", "未知"]
gy = [
    rates.count(1),
    rates.count(2),
    rates.count(3)
]
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add("", list(zip(gx, gy)))
    .set_global_opts(title_opts=opts.TitleOpts(title="性别比例", subtitle="数据来源：猫眼电影", pos_left = "left"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render_notebook()

# 位置分布
cities = []
for city in df.iloc[:, 1]:
    if city != "":
        cities.append(city)
data = Counter(cities).most_common(100)
gx1 = []
gy1 = []
for c in data:
    gx1.append(c[0])
    gy1.append(c[1])
geo = Geo(init_opts=opts.InitOpts(width="700px", height="400px", theme=ThemeType.DARK, bg_color="#404a59"))
(
    geo.add_schema(maptype="china", itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"))
    .add("评论数量", list(zip(gx1, gy1)))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
       toolbox_opts=opts.ToolboxOpts,
       title_opts=opts.TitleOpts(title="位置分布地理坐标", subtitle="数据来源：猫眼电影", pos_left = "left"),
       visualmap_opts=opts.VisualMapOpts(max_=500, is_piecewise=True)
    )
).render_notebook()

# 根据城市数据生成柱状图
data_top15 = Counter(cities).most_common(15)
gx2 = []
gy2 = []
for c in data_top15:
    gx2.append(c[0])
    gy2.append(c[1])
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(gx2)
    .add_yaxis("", gy2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="城市来源 TOP15", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

# 各个时间段的评论数量
times = df.iloc[:, 5]
hours = []
for t in times:
    hours.append(str(t[11:13]))
hdata = sorted(Counter(hours).most_common())
hx = []
hy = []
for c in hdata:
    hx.append(c[0])
    hy.append(c[1])
(
    Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(hx)
    .add_yaxis("", hy, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="24小时评论数量", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

# 人物提及次数
cts_list = df.iloc[:, 2]
cts_str ="".join([str(i) for i in cts_list])
px = ["黄渤", "王宝强", "刘昊然", "葛优", "刘敏涛", "范伟", "张译", "邓超", "闫妮", "沈腾", "马丽"]
py = [cts_str.count("黄渤") + cts_str.count("黄大宝"), cts_str.count("王宝强") + cts_str.count("老唐"),
      cts_str.count("刘昊然") + cts_str.count("小秦"), cts_str.count("葛优") + cts_str.count("张北京"),
      cts_str.count("刘敏涛") + cts_str.count("玲子"), cts_str.count("范伟") + cts_str.count("老范"),
      cts_str.count("张译") + cts_str.count("姜前方"), cts_str.count("邓超") + cts_str.count("乔树林"),
      cts_str.count("闫妮") + cts_str.count("闫飞燕"), cts_str.count("沈腾") + cts_str.count("马亮"),
      cts_str.count("马丽") + cts_str.count("秋霞")]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(px)
    .add_yaxis("", py)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="主要演员及其饰演角色被提及次数", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

# 电影单元被提及次数
mx = ["天上掉下个UFO", "北京好人", "最后一课", "回乡之路", "神笔马亮"]
my = [cts_str.count("天上掉下个UFO"), cts_str.count("北京好人"), cts_str.count("最后一课"), cts_str.count("回乡之路"), cts_str.count("神笔马亮")]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(mx)
    .add_yaxis("", my)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="电影单元被提及次数", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()
