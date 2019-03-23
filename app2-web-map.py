import folium
import pandas

data = pandas.read_csv("spotonmap.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

map = folium.Map(location=[55.753220, 37.618068], zoom_start=15)

fgv = folium.FeatureGroup(name="Spotonmap")

for lt, ln, name in zip(lat, lon, name):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(name), icon=folium.Icon(color = 'green')))

map.add_child(fgv)

map.save("Map1.html")
