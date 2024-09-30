# 로우 인덱싱
# loc: label 기준 인덱싱
# iloc: index 기준 인덱싱
import seaborn as sns
import pandas as pd

print(sns.__version__)

iris = sns.load_dataset("iris")

print(iris.head(1))  #데이터 잘 불러왔는지 첫 줄 통해 확인

print(iris.loc[[0,5], :])  #loc.[행, 열] 

print(iris.loc[[0,9],["sepal_width", "species"]])  #가독성이 좋음

print(iris.iloc[[0,9], [1,4]])  #위와 같음, but index 숫자를 알아야 함 & 직관적이지 않음 ==> loc 쓰는거 추천

# 조건식
# 값을 가져오고 싶다면, True 값만 가져오면 됨
print(iris['sepal_width'] > 4.0)
print(iris.loc[iris['sepal_width'] > 4.0, :])  #조건에 맞는 데이터 추출, 하지만 index는 이전과 같음 즉, 완전하게 index 정렬 안된 상태

# 조건에 맞는 값들 가져와서 인덱스 정렬하는 법
print(iris.loc[iris['sepal_width'] > 4.0, :].reset_index())   #이러면 새 index부여받았지만 원래 index 남아있어서 drop시킴 (아래)

print(iris.loc[iris['sepal_width'] > 4.0, :].reset_index(drop=True)) 

# 다중 조건
get_petal = iris.loc[(iris['petal_length']> 1.4)&(iris['petal_width']>0.4), :].reset_index(drop=True)  #petal길이 1.4초과 & petal너비 0.4초과 추출
print(get_petal)

# 문자열 기반 추출
get_setosa = iris.loc[(iris['species']=='setosa')&(iris['petal_width']>0.5),:].reset_index(drop=True)  #종류 setosa & petal너비 0.5초과 추출
print(get_setosa)

print(iris['species'].unique())  #species 종류 추출

# 새로운 column 추가
iris2 = iris.copy()
iris2['newCol'] = 0  # 새로운 column 추가
iris2['sepal_sum'] = iris2['sepal_length'] + iris2['sepal_width']  # 연산해서 column 추가 됨
print(iris2.head(1))

# 삭제
data = [
    ["알파코", 10000000, 10.05], 
    ["A", 500000, 1.05], 
    ["B", 1000, 1.28]
]

index = ["039900", "039910", "039901"]
columns = ["종목명", "현재가", "등락률"]
df = pd.DataFrame(data=data, index=index, columns=columns)

# aixs = 0 : 행 처리 // axis = 1 : 열 처리
df2 = df.drop("039900", axis=0)  #인덱스가 "039900"인 가로 행 삭제
print(df2)
df3 = df.drop("종목명", axis=1)  #"종목명" 세로 열 삭제
print(df3)

# 컬럼 명 변경

data = [
    ["알파코", 10000000, 10.05], 
    ["A", 500000, 1.05], 
    ["B", 1000, 1.28]
]

index = ["039900", "039910", "039901"]
columns = ["종목명", "현재가", "등락률"]
df = pd.DataFrame(data=data, index=index, columns=columns)

df2 = df.rename(columns={'종목명' : 'code', '현재가' : 'current_price'})   #데이터프레임.rename(columns={'이전 이름' : '바꿀 이름'})
print(df2)

# 연습 문제 : 문자형 자료 정수형으로 바꾸기

data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = pd.DataFrame(data=data, columns=columns)
print(df)

res = df.map(lambda x: int(x.replace(',','')))
print(res)
print(type(res.loc[1,"03/02"]))