import folium
import pandas as pd

sample_data = pd.read_csv('data\\data3.csv', sep=',')
print sample_data.shape
print sample_data.head()
print sample_data.columns
sample_data.columns = ['sec', 'road', 'road_detail', 'lon', 'lat', 'extra']
print sample_data.columns

shilin = [25.084768, 121.524986]
zoom = 12

map_osm = folium.Map(location=shilin, zoom_start=zoom)
for i in range(len(sample_data)):
    message = '%s->%s' % (sample_data.iloc[i, 1], sample_data.iloc[i, 2])
    message_utf8 = unicode(message, 'utf-8')
    coord = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    icon1 = folium.Icon(color='blue', icon='info-sign')
    folium.Marker(coord, icon=icon1, popup=message_utf8).add_to(map_osm)

circle1 = [25.072839, 121.588347]
folium.CircleMarker(circle1, radius=200, popup='NeiHu',
                    fill_color='#C0FFEE').add_to(map_osm)
folium.Circle(shilin, radius=200, popup='NeiHu',
              fill_color='#C0FFEE').add_to(map_osm)

map_osm.save('map\\demo76.html')
