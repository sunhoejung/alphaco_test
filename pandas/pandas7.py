#pandas 기초 문법 2
import pandas as pd

data = [
    [1416, 1416, 2994, 1755],
    [6.42, 17.63, 21.09, 13.93],
    [1.10, 1.49, 2.06, 1.88]
]

columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
index = ["DPS", "PER", "PBR"]

df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
print(df.info())

# filter 
print(df.filter(items=['2018/12']))  #2018/12 행만 조회

print(df.filter(items=['PER'], axis=0))  #PER 열만 조회

#정규표현식으로 활용해서 행과 열을 조회
print(df.filter(regex='2020'))  #2020이 들어간 행 혹은 열만 조회

#R이 들어간 행만 조회
print(df.filter(regex='R', axis=0))

#R로 '끝나는' 행 조회
print(df.filter(regex='R$', axis=0))

