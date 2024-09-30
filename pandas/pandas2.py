# 데이터 프레임 생성
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)

# 첫 번째 방법: 리스트 활용
# 두 번째 빵법: 딕셔너리 활용
#리스트
data = [
    ["039900", "알파코", 1000000, 10.05], 
    ["039910", "A", 500000, 1.05], 
    ["039920", "B", 1000, 1.28]
]

columns = ["종목코드", "종목명", "현재가", "등락률"]
df = pd.DataFrame(data = data, columns=columns)
print(df)

#딕셔너리
data2 = {
    "종목코드" : ["039900", "039910","039920"], 
    "종목명" : ["알파코", "A", "B"]
}

df2 = pd.DataFrame(data = data2)
print(df2)

data2 = {
    "종목코드" : ['039900', '039910', '039920'], 
    "종목명" : ["알파코", "A", "B"], 
    "현재가" : [10000000, 500000, 1000], 
    "등락률" : [10.05, 1.05, 1.28]
}

df2 = pd.DataFrame(data = data2)
print(df2)

#해당되는 종목 인덱스로 변경
df2 = df2.set_index("종목코드")  #종목 코드가 인덱스가 됨
print(df2)

df2.reset_index()  #원래의 인덱스로 돌아감
print(df2)

df2.reset_index(drop=True)  #drop
print(df2)

data = [
    ["알파코", 10000000, 10.05], 
    ["A", 500000, 1.05], 
    ["B", 1000, 1.28]
]

index = ["039900", "039910", "039900"]
columns = ["종목명", "현재가", "등락률"]
df = pd.DataFrame(data=data, index=index, columns=columns)   #index값 따로 부여
print(df)

print(df.index)  #numpy 형태로 출력

print(df.index.shape)   #1차원배열 3 1

print(df.values)  #numpy 형태로 출력

print(df.values.shape)   #2차원 배열 3 3 

# 각각의 column에 접근

print(df.현재가)  #시리즈 형태

print(df['현재가'])  #데이터 프레임 형태

print(df[['현재가']])

