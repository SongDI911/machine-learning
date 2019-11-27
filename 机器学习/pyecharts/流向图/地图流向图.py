from pyecharts import  Map
import random
value = [120, 110]
attr = [u'河南', u'湖南']
value1 = [100,300]
attr1 = ['安徽','四川']
map = Map(u"Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype=u"china", is_visualmap=True, visual_text_color='#000')
map.add("", attr1, value1, maptype=u"china", is_visualmap=True)
map.render('./map.html')
