import folium
import os

# 创建一个Folium地图对象，设置中心点和缩放级别
m = folium.Map(location=[55.8713, -4.2996], zoom_start=18)

# 添加OpenStreetMap图层（也可以使用其他图层，具体取决于需求）
folium.TileLayer("openstreetmap").add_to(m)

# 获取地图数据并保存为PNG文件
map_data = m._to_png()
output_file = "glasgow_map.png"

with open(output_file, "wb") as f:
    f.write(map_data)

print(f"Map saved to {output_file}")
