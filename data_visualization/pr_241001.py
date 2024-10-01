import matplotlib.pyplot as plt
import pandas as pd

estate = pd.read_csv("seoul_real_estate.csv")

print(estate.head(1))

'''
## 자치구별 부동산 거래 건수 비교 (Bar Chart)
- hint : matplotlib.pyplot.bar
- SGG_NM을 기준으로 각 자치구별로 부동산 거래가 몇 건 이루어졌는지 bar 차트로 나타내세요. 
'''
#방법1
count_df = estate['SGG_NM'].value_counts()   #데이터 수집

print(count_df, type(count_df))   #타입: 시리즈

index_count_df = count_df.index.to_list()   #데이터 가공
list_count_df = count_df.to_list()

fig, ax = plt.subplots()   #시각화
ax.bar(index_count_df, list_count_df)

plt.show()

#방법2
자치구 = list(count_df.index)   #데이터 가공
건수 = list(count_df.values)

fig, ax = plt.subplots()   #시각화
ax.bar(자치구, 건수)
plt.show()


'''
## 건물 면적 대비 거래 가격 관계
- BLDG_AREA와 OBJ_AMT 간의 관계를 산점도로 시각화하세요.
- matplotlib.pyplot.scatter
'''

fig,ax = plt.subplots()
ax.scatter(estate['BLDG_AREA'], estate['OBJ_AMT'], alpha=0.5)
plt.show()



