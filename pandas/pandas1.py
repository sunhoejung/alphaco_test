#Pandas Series
import pandas as pd
import numpy as np

print(pd.__version__)

data = [10,20,30]
s = pd.Series(data)
print(s)
print(type(s))

data = np.arange(5)
s = pd.Series(data)
print(s)     #잘됨 // pandas랑 numpy 유사

data = np.arange(5)
s = pd.DataFrame(data)
print(s)    #출력물 Series랑 좀 다름

data = ["시가", "고가"]
s = pd.Series(data)
print(s)

data = [80000, "90000"]
s = pd.Series(data)
print(s)    #dtype: object  // 어떤 형식이 아직 정해지지 않은 상태 (여러 데이터 섞여있어서) -> 나중에 변경, 처리해줘야 됨 (형변환)

# 시리즈 인덱스

data = [1000, 2000, 3000]
s = pd.Series(data)
print(s.index)   #RangeIndex(start=0, stop=3, step=1)  // 이 또한 하나의 객체다
# 위 형태 말고 리스트 형태로 인덱스 얻으려면
#1
print(list(s.index))   #[0, 1, 2]
#2
print(s.index.to_list())   

# 시리즈 생성하면서 인덱스도 같이 생성
data = [1000, 2000, 3000]
index = ["A", "B", "C"]

s = pd.Series(data, index)
print(s)    #index 리스트가 순서대로 인덱스 됨

print(s.values, type(s.values))  # [1000 2000 3000] <class 'numpy.ndarray'>  => numpy 배열

print(s.values.reshape(3,1))   #numpy 배열이니까 numpy 메소드도 사용가능

# 시리즈 인덱싱

print(s.iloc[0])  #1000  // 
print(s.iloc[1])  #2000
print(s.iloc[2])  #3000
#iloc는 0번째,1번째 등 인덱스 번호로 처리  // Integer-location based

print(s.loc["A"])  #1000  // loc에 index 숫자로 쓰면 키에러 발생
#loc를 쓰면 인덱스의 값(value)을 통해서 접근  // Label(이름) or Boolean Array based

# 시리즈 생성하면서 인덱스도 같이 생성
data = [1000, 2000, 3000]

s2 = pd.Series(data=data)
print(s2.iloc[0])  #1000            // iloc에서의 0은 위치 0을 의미
#print(s2.loc[0])  #키 에러 발생    //  loc에서의 0은 라벨 0을 의미  // 필터링할 때는 loc 기본으로 사용
#print(s2.loc["A"])  #키 에러 발생 // 이유: s2의 인덱스는 0,1,2 고유 번호고 label 부여받은 게 없다. 

# 슬라이싱
print(s.iloc[0:2])  #기존의 인덱싱처럼 0,1 나옴
print(s.loc["A":"B"])  #"A", "B" 둘 다 나옴 즉, 기존 인덱싱이랑 다름

# 시리즈 수정/추가/삭제

s.loc["B"] = 500  #딕셔너리 key값 인덱스 통해 value 수정하는 것과 비슷함
print(s)  #B의 가격 2000에서 500으로 수정됨

s.iloc[0] = 1500  #마찬가지로 변경되지만 loc가 좀 더 직관적임

s['C'] = 2800  #이것도 수정됨. 하지만 추천X

# 시리즈 연산

evan = pd.Series([10,20,30], index=['NAVER', 'APPLE', 'NVDIA'])
jenny = pd.Series([10,30,20], index=['NVDIA', 'NAVER', 'APPLE'])

# 총 보유하고 잇는 주식의 숫자를 계산

print(evan+jenny)   #인덱스 순서가 달라도 같은 인덱스끼리 연산되게 해줌  // 더한 값의 출력 인덱스는 유니코드 순으로

evan = pd.Series([10,20,30], index=['NAVER', 'APPLE', 'NVDIA'])
jenny = pd.Series([10,30,20], index=['NVDIA', 'NAVER', 'SAMSUNG'])  #인덱스 라벨 하나씩 달라짐

print(evan+jenny)  #다른 라벨의 인덱스의 값은 NaN이 나옴

# 최대 최소 메소드

date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = pd.Series([42800, 42700, 42050, 42950, 43000], index=date)  #매도
low = pd.Series([42150, 42150, 41300, 42150, 42350] , index=date)  #매수

diff = high - low
diff.idxmax()  #최대값의 인덱스 리턴하는 메소드
diff.idxmin()  #최소값의 인덱스 리턴하는 메소드
diff[diff.idxmax()]  #최대값 리턴
diff[diff.idxmax()]  #최소값 리턴

profit = high / low  #단순 수익률
print(profit)
profit.cumprod()
print(profit.cumprod())  #profit과 다름  // 누적 개념

# 시리즈와 Map

s = pd.Series(['1,234', '5,678', '12,345'])
#정수형으로 바꾸려면 에러 발생 -> ','없애고 정수형으로

def rm_comma(x):  #사용자 정의 함수와 map 통해 반복문 안쓰고 정수형으로 바꿈
    return int(x.replace(',',''))

result = s.map(rm_comma)
result2 = s.map(lambda x: int(x.replace(',','')))  #람다로 해도 됨
print(result)
print(result2)

#위와 비슷한 예

def remove_dollar_sign(x):
    return float(x.replace('$', '').replace(',', ''))
s = pd.Series(['$1,234.56', '$5,678.90', '$12,345.67'])
result = s.map(remove_dollar_sign)

#위와 비슷한 예 2
#기준점 13으로 크다 작다 나오게
s = pd.Series([5,10,15,20])

def bigger_13(x):
    if x > 13:
        return f'{x}는(은) 13보다 크다'
    elif x == 13:
        return f'{x}은 13과 같다'
    else:
        return f'{x}는(은) 13보다 작다'
    
result = s.map(bigger_13)  # 람다: s.map(lambda x: '크다' if x ㄴ> 13 else '작다')
print(result)

# 필터링

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
s = pd.Series(data=data, index=index)

cond = s > 42000
print(cond)  #결과값 boolean
print(s[cond])  #해당되는 값만 가져옴

#코드 간결하게 하려면
print(s[s>42000])

#문제 : 종가가 시가보다 높은 날을 구하라

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = pd.Series(data=open, index=index)  #시작가
close = pd.Series(data=close, index=index)  #종료가

print(close[open < close].index)
