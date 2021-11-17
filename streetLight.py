# CSV 파일 열기
import pandas as pd
file = r'C:\Users\user\Desktop\web_AI\python_code\서울특별시_용산구_보안등정보.csv' ####본인 파일위치 입력#####
file = file.replace('\\','//')
#print(file)
street_csv = pd.read_csv(file,encoding='cp949')
print(street_csv.head())

# 데이터프레임 NaN 값 대체
street_csv = street_csv.fillna(0.0)
print(street_csv.head())

# x좌표(위도),y좌표(경도), 이름 리스트로 만들기
x1 = []
y1 = []
name = []
for i in range(len(street_csv['위도'])):
    if street_csv['위도'][i] == 0.0 or street_csv['경도'][i] == 0.0:
        pass
    else:
        name.append(street_csv['보안등위치명'][i])
        x1.append(street_csv['위도'][i])
        y1.append(street_csv['경도'][i])
print('이름갯수: ',len(name))
print('x갯수: ',len(x1))
print('y갯수: ',len(y1))