from pyecharts import Map
#
# value = [155, 10, 66, 78]
# attr = ["福建", "山东", "北京", "上海"]
attr =['test']
value =[[120.004217,24.000183]]
map = Map("全国地图示例", width=1200, height=600)
map.add("",attr,value, maptype='china',is_visualmap=True,visual_text_color='#000')
map.render()
