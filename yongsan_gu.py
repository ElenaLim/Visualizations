import folium
import json
#map 만들기
map_osm = folium.Map(location=[37.538821, 126.98368841130002],zoom_start=14)
#geojson파일 오픈
file_name= r'C:\Users\user\Downloads\yongsan.zip.geojson' ####본인 파일위치 입력#####
file_name = file_name.replace('\\','/')
with open(file_name, 'rt') as f:
    geo = json.load(f)
    f.close()
folium.GeoJson(geo, name='YongSan').add_to(map_osm)

#map_osm.save('test2.html')

