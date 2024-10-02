# 날짜 형 변환하기 (초기 타입: object)

import pandas as pd

df1 = pd.read_excel("ss_ex_1.xlsx")
print(df1.info())
print(df1.head(1))

df1['일자'] = pd.to_datetime(df1['일자'])  #'일자'열을 datetime 형식으로 변환하여 날짜 쉽게 처리하기 위함
print(df1.info())
print(df1.head(1))

df2 = pd.read_excel("ss_ex_1.xlsx" , index_col=0)  #index_col=0 통해 첫번째 열을 인덱스로 설정
print(df2.head(1))

df2.index = pd.to_datetime(df2.index)  #첫번째 열이 날짜열이니 datetime으로
print(df2.head(1))
print(type(df2.index))

df3 = pd.read_excel("ss_ex_1.xlsx" , parse_dates=['일자'])  #parse_dates를 통해 특정 열(요기선 '일자')을 읽을 때 바로 datetime 형식으로 변환
df3 = df3.sort_values('일자')  #'일자'열 기준으로 데이터 정렬
print(df3.info())
print(df3)

#'일자'열 datetime 형식으로 변환하는 동시에 첫번째 열 인덱스로 설정함
df4 = pd.read_excel("ss_ex_1.xlsx", parse_dates=['일자'], index_col=0)  #시리얼 데이터 부를 때 권장 방식
df4 = df4.sort_index(ascending=True)
print(df4.info())
print(df4.head())



