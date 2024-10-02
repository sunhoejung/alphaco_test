# 정렬
import pandas as pd

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = pd.DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)
print(df)
print(df.info())

print(df.sort_values(by="현재가", ascending=True))
print(df.sort_values(by="현재가", ascending=False))  #ascending)True: 오름차순 / False: 내림차순

print(df.sort_values(by="종목명", ascending=True))
print(df.sort_values(by="종목명", ascending=False))  #문자는 유니코드 순 정렬

print(df.sort_index())  #기본값
print(df.sort_index(ascending=False))  #역순

# 인덱스 연산 - 집합 연산을 이용해서 데이터 병합을 할 때 사용
idx1 = pd.Index([1,2,3])
idx2 = pd.Index([2,3,4])

print(idx1.union(idx2))  #합집합
print(idx1.intersection(idx2))  #교집합
print(idx1.difference(idx2))  #차집합

# groupby 연산
# groupby - split-apply-combine / 하나의 데이터 각 그룹 단위로 쪼개서 연산(합계,평균 등 함수 적용) 후 결합
data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = pd.DataFrame(data=data, columns=columns)
print(df)

result = df.groupby("테마")[["PER", "PBR"]]
print(result, type(result))  #타입: DataFrameGroupBy

result1 = df.groupby("테마")[["PER", "PBR"]].mean()
print(result1, type(result1))  #mean() 쓰면 DataFrame 타입으로 반환

print(df.groupby("테마").get_group("2차전지(생산)"))  #groupby(a).get_group(b) : a 칼럼 같은 b끼리 그룹화
print(df.groupby("테마").get_group("시스템반도체"))
print(df.groupby("테마").get_group("해운"))





df = pd.read_excel("ss_ex_1.xlsx", parse_dates=['일자'], index_col=0)
df = df.reset_index()  #인덱스 초기화되고 '일자' 칼럼 생성됨
print(df.head(1))
print(df.info())  #일자 칼럼 타입 datetime64
print(df['일자'].dt.quarter)  #quarter: 분기 반환  / datetime class의 attribute
print(df['일자'].dt.year)  #year: 연도 반환
print(df['일자'].dt.month)  #month: 월 반환
print(df['일자'].dt.day)  #day: 일 반환

#분기, 연도, 월, 일 - 칼럼 추가 // 목적: 분류별 집계
df_quarter = df['일자'].dt.quarter
df['분기'] = df_quarter
df_year = df['일자'].dt.year
df['연도'] = df_year
df_month = df['일자'].dt.month
df['월'] = df_month
df_day = df['일자'].dt.day
df['일'] = df_day
print(df.info())

result = df.groupby(['연도', '월']).get_group((2021, 2))  #2021년 2월만 뽑아서 그룹화
print(result)

result = df.groupby(['연도', '월'])['시가'].sum()  #연도, 월별 시가 합계 정리
print(result)

result = df.groupby(['연도', '월'])['시가'].mean()  #연도, 월별 시가 평균 정리
print(result)

multiples = {"시가" : "first", "저가" : min, "고가" : max, "종가" : "last"}  #왼쪽: 칼럼 / 오른쪽: 방법

result = df.groupby(['연도', '월', '일']).agg(multiples)  #시가, 저가, 고가, 종가 월별로 집계해서 반환
print(result)
print(result.reset_index())  #index reset하는 이유: index가 2개 생김 (연도, 월)