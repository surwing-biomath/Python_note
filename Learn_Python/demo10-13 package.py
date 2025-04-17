# PyEcharts是由百度开源的数据可视化库，它对流程图的支持度比较高，给用户提供了30多种图形，如柱形渐变图、K线周期图等。
# 中文帮助文档：https://pyecharts.org/#/zh-cn/
# PyEcharts的使用方法：
# 1.安装：pip install pyecharts
# 2.导入：from pyecharts import options as opts
# 3.创建图表对象：from pyecharts.charts import Line, Bar, Pie, Map, Geo, WordCloud, Funnel, Gauge, Radar, Liquid, TreeMap, Sunburst, Sankey, Boxplot
# 4.设置图表类型：如Line()、Bar()、Pie()等
# 5.设置图表数据：如.add_xaxis()、add_yaxis()等
# 6.设置图表样式：如.set_global_opts()、set_series_opts()等
# 7.渲染图表：如.render()、render_notebook()等
# 8.保存图表：如.render(path)等
# 9.显示图表：如.render_notebook()等
# 11.设置图表标题：如.set_global_opts(title="标题")等
# 12.设置图表颜色：如.set_series_opts(color="red")等
# 13.设置图表大小：如.set_global_opts(width=800, height=600)等
# 14.设置图表位置：如.set_global_opts(left="10%", top="10%")等
# 15.设置图表字体：如.set_global_opts(font_family="Arial")等
# 16.设置图表字体大小：如.set_global_opts(font_size=12)等
# 17.设置图表字体颜色：如.set_global_opts(font_color="red")等
# 18.设置图表字体粗细：如.set_global_opts(font_weight="bold")等
# 19.设置图表字体斜体：如.set_global_opts(font_style="italic")等
# 20.设置图表字体下划线：如.set_global_opts(font_underline=True)等
# 21.设置图表字体删除线：如.set_global_opts(font_strike=True)等
# 22.设置图表字体阴影：如.set_global_opts(font_shadow=True)等
# 23.设置图表字体阴影颜色：如.set_global_opts(font_shadow_color="red")等
# 24.设置图表字体阴影模糊度：如.set_global_opts(font_shadow_blur=5)等
# 25.设置图表字体阴影偏移：如.set_global_opts(font_shadow_offset_x=5, font_shadow_offset_y=5)等
# 26.设置图表字体阴影透明度：如.set_global_opts(font_shadow_opacity=0.5)等
# 27.设置图表字体阴影混合模式：如.set_global_opts(font_shadow_blend_mode="normal")等
# 28.设置图表字体阴影混合模式透明度：如.set_global_opts(font_shadow_blend_mode_opacity=0.5)等
# 29.设置图表字体阴影混合模式颜色：如.set_global_opts(font_shadow_blend_mode_color="red")等
# 30.设置图表字体阴影混合模式模糊度：如.set_global_opts(font_shadow_blend_mode_blur=5)等
# 31.设置图表字体阴影混合模式偏移：如.set_global_opts(font_shadow_blend_mode_offset_x=5, font_shadow_blend_mode_offset_y=5)等
# 32.设置图表字体阴影混合模式透明度：如.set_global_opts(font_shadow_blend_mode_opacity=0.5)等

# 1,导入pyecharts包；2，找到相应图形模板；3，准备相应数据；4，对图表进行个性化修饰

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

lst = [
    ["直接访问", 335], ["邮件营销", 310], ["联盟广告", 234], ["视频广告", 135], ["搜索引擎", 1548], ["其他", 335]
]

c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", lst, radius=["30%", "70%"], center=["50%", "50%"])
    .set_colors(["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"])
    .set_global_opts(title_opts=opts.TitleOpts(title="各渠道访问量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("channel.html")
)
