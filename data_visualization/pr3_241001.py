import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

estate = pd.read_csv("seoul_real_estate.csv")
'''
2:23
## 자치구별 부동산 거래 건수 비교 (Bar Chart)
- hint : seaborn.barplot
- SGG_NM을 기준으로 각 자치구별로 부동산 거래가 몇 건 이루어졌는지 bar 차트로 나타내세요.
'''
print(estate.head(1))
#포인트: seaborn은 dataFrame 형태로 만든다 (index가 0,1,2,.. 로 되어있는 형태)
sgg_count = estate['SGG_NM'].value_counts().reset_index()  #seaborn은 가급적 index 0으로 만드는 게 좋음  이유:seaborn은 column명을 써줘야 해서 & dataframe형태로 변환
#value_counts하면 시리즈 형태 나옴. 이를 reset_index통해서 데이터프레임 형태로 가공
print(sgg_count)
sgg_count.columns = ['sgg', 'count']

sgg_count.head(1)

fig, ax = plt.subplots()
sns.barplot(sgg_count, x='sgg', y='count')
plt.xticks(rotation=45)  #x축 글자 회전
plt.show()


'''
## 건물 면적 대비 거래 가격 관계
- BLDG_AREA와 OBJ_AMT 간의 관계를 산점도로 시각화하세요.
- sns.scatterplot (편집됨) 
'''

fig,ax = plt.subplots()
sns.scatterplot(data=estate, x='BLDG_AREA', y='OBJ_AMT', alpha=0.5)
plt.show()

#자료 내 특정 범위 색깔 설정

highest_values = estate['BLDG_AREA'] >= 900  #900이상 빨간색으로 강조 위한 변수 설정

fig,ax = plt.subplots()
sns.scatterplot(data=estate, x='BLDG_AREA', y='OBJ_AMT', alpha=0.5)   #seaborn
ax.scatter(estate['BLDG_AREA'][highest_values], estate['OBJ_AMT'][highest_values], color = 'red')   #matplob  // 900이상 빨간색으로 강조
plt.show()