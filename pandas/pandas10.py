# 데이터 프레임 합치기

import pandas as pd

# concat

# 첫번째 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index = ["2019-06-21", "2019-06-20"]
df1 = pd.DataFrame(data, index=index)
print(df1.head())

# 두번째 데이터프레임
data = {
    '종가': [110000, 483689],
    '거래량': [109000, 791946]
}
index = ["2019-06-19", "2019-06-18"]
df2 = pd.DataFrame(data, index=index)
print(df2.head())

result = pd.concat([df1, df2])  #데이터프레임 합치는 메소드
#concat은 데이터를 상하로 이어붙이는 개념 / df1,df2 순서 바뀌면 result의 순서도 바뀜
#합치고 난 뒤 Nan뜨면 둘 중 하나가 column이 부족한 것
#합치고 데이터 정리하기 보단, 정리하고 나서 합치는 게 훨씬 편하다

result.sort_index(ascending=False)
print(result)

# merge

# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["전기전자", "000660", "SK하이닉스", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = pd.DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종", "등락률"]
df2 = pd.DataFrame(data=data, columns=columns)

merge1 = pd.merge(left = df1, right = df2, on = "업종")  #업종을 기준으로 병합
#교차하는 것만 뽑음 (sql join과 비슷한 개념)
print(merge1)



data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "037590", "카카오", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = pd.DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종", "등락률"]
df2 = pd.DataFrame(data=data, columns=columns)

df3 = pd.merge(left = df1, right = df2, how = 'left', on = '업종')
#기준 테이블 df1 / 서비스업 등락률에 Nan 나옴 / 서비스업은 df2에 없어서
print(df3)

df4 = pd.merge(left = df1, right = df2, on = '업종')
#Nan 안생김 / how 안쓰면 매칭되는 것만 가져옴
print(df4)

df5 = pd.merge(left = df1, right = df2, how = 'right', on = '업종')
#df2가 기준 테이블이라이라 은행, 보험의 종목코드, 종목명, 현재가는 Nan
print(df5)

df6 = pd.merge(left = df1, right = df2, how = 'outer', on = '업종')
# 전체 가져옴
print(df6)

# 다른 케이스

data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "037590", "카카오", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = pd.DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["항목", "등락률"]
df2 = pd.DataFrame(data=data, columns=columns)

#df6 = pd.merge(left = df1, right = df2, how = 'outer', on = '업종')
#키에러 뜸 / 이유: column 명이 달라서 / 처리 전 맞춰주는게 좋음

#해결법 (cf. 권장 방법은 기준 칼럼 명 미리 맞추기)
df6 = pd.merge(left = df1, right = df2, how = 'left', left_on = '업종', right_on = '항목')
print(df6)

# join

data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "037590", "카카오", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = pd.DataFrame(data=data, columns=columns)
df1 = df1.set_index("업종")
print(df1)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["항목", "등락률"]
df2 = pd.DataFrame(data=data, columns=columns)
df2 = df2.set_index("항목")
print(df2)

df3 = df1.join(other = df2)
print(df3)

# merge 기본값 : inner join
# join = 기본값 : left join
# 기본값 있지만 how 통해서 명시적으로 써주는게 좋음

df4 = df1.join(other = df2, how = 'left')  #left,right,outer,inner
print(df4)

# 예제 : groupby 통해 시가총액 평균 구하기
data = [
    ["2017", "삼성", 500],
    ["2017", "LG", 300],    
    ["2017", "SK하이닉스", 200],
    ["2018", "삼성", 600],
    ["2018", "LG", 400],
    ["2018", "SK하이닉스", 300],    
]

columns = ["연도", "회사", "시가총액"]
df = pd.DataFrame(data=data, columns=columns)
print(df, df.info())

result = df.groupby(['연도'])['시가총액'].mean().to_frame()  #데이터프레임으로 만듦
result.columns = ['시가총액평균']

df = df.join(result, on='연도')  #on= 연도 넣어야 시가총액평균 Nan으로 안 뜸 / result의 연도가 칼럼이 아님 인덱스라서
#아님 reset_index 등으로 미리 맞춰줌

print(df)
