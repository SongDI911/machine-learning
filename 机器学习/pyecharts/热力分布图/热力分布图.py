from pyecharts import Geo
data = [
("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)]

attr, value = Geo.cast(data)

geo = Geo("全国主要城市空气质量热力图", "data from pm2.5")

geo.add("空气质量热力图", attr, value, visual_range=[0, 25], type='heatmap',visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./04-04空气质量热力图.html")