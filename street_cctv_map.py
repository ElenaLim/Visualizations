# CSV 파일 열기
import pandas as pd
file = r'C:\Users\user\Desktop\web_AI\python_code\yongsan_CCTV.csv'  ####본인 파일위치 입력#####
file = file.replace('\\','//')
#print(file)
cctv_csv = pd.read_csv(file,encoding='cp949')
print(cctv_csv.head(5))

# 데이터프레임 NaN 값 대체
cctv_csv = cctv_csv.fillna(0.0)
print(cctv_csv.head())

# x좌표(위도),y좌표(경도) 리스트로 만들기
x = []
y = []
for i in range(len(cctv_csv['WGS x좌표'])):
    if cctv_csv['WGS x좌표'][i] == 0.0 or cctv_csv['WGS y좌표'][i] == 0.0:
        pass
    else:

        x.append(cctv_csv['WGS x좌표'][i])
        y.append(cctv_csv['WGS y좌표'][i])
print('x갯수: ',len(x))
print('y갯수: ',len(y))



#지도 생성 및 marker 지정하기
import folium
import folium.plugins as plug
from streetLight import x1,y1,name
from yongsan_gu import geo
map_osm = folium.Map(location=[37.538821, 126.98368841130002],zoom_start=14)
marker_cluster = plug.MarkerCluster().add_to(map_osm)
folium.GeoJson(geo, name='YongSan').add_to(map_osm)

for i in range(len(x)):

    folium.Marker([x[i],y[i]], popup='용산CCTV_%d'%i, icon=folium.Icon(color='red', icon='ok-circle')).add_to(marker_cluster)

for i in range(len(x1)):
    folium.Marker([x1[i],y1[i]], popup= name[i], icon=folium.Icon(color='orange', icon='star')).add_to(marker_cluster)


#map저장
map_osm.save('YONGSAN.html')