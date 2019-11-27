from pyecharts import Pie
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
pie = Pie("饼状图",title_pos='center',width=900)
pie.add('降水量',columns,data1,is_legend_show=False)
pie.add('蒸发量',columns,data2,is_label_show=True,is_legend_show=False)
pie.render()
