from pyecharts import Bar
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# 设置主标题和副标题
bar = Bar("柱状图","一年蒸发量与降水量")

# 添加变量名称,x轴，y轴
# bar.add("降水量",columns,data1)
# bar.add("蒸发量",columns,data2)

# 添加平均线,要写成list的形式 mark_line画线  mark_point选点显示最大值和最小值   is_label_show是否显示数据
bar.add("降水量",columns,data1,mark_line=['average'],mark_point=['max','min'],is_label_show=True,is_legend_show=True)
bar.add("蒸发量",columns,data2,mark_line=['average'],mark_point=['max','min'],is_label_show=True,is_legend_show=True)
bar.render()

