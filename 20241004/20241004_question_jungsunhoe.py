# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly
import yfinance as yf
import plotly.graph_objects as go

# 서술형 문제 1
"""
1. github new repository 생성
2. 설정: public/add .gitignore python
3. git bash 실행
4. git clone "url"(shift insert)
5. 경로에 폴더 생성됨
6. main.py 작성  중요)pwd 통해서 경로 확인 잘하기!
7. (업데이트) git add . / git commit -m "test" / git push
8. github에 업데이트 완료
"""

# 코드 문제 1
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * 2)
print(result)

# 답지
code_result1 = [i*2 for i in range(10) if i%2==0]
print(code_result1)

# 코드 문제 2
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# 답지
keys = list(my_dict.keys())
values = list(my_dict.values())

for key, value in zip(keys, values):
    print(f'{key}: {value}')

# 코드 문제 3
series = pd.Series([25, 35, 45, 60, 75])

# 답지
# np.where를 사용하여 조건 적용
code_result3 = np.where((series>30)&(series<60), series+10, series)

# 결과 출력
list_series = list(code_result3)
for i in range(len(list_series)):
    print(f'{i}     {list_series[i]}')
print(type(series[0]))

# 코드 문제 4
iris = sns.load_dataset("iris")

# 답지
# 여기서부터 코드 작성

iris.to_csv("output/code4_jungjihoon.csv", index=True)
iris.to_excel("output/code4_jungjihoon.xlsx", index=True)




# 코드 문제 5
data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = pd.DataFrame(data=data, columns=columns)
df.info()

# 답지
# 여기서부터 코드 작성

def rm_comma(x):
    return int(x.replace(',', ''))

res = df[['03/02', '03/03']].map(rm_comma)
print(res.info())
# 코드 문제 6
apple = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
fig, ax = plt.subplots()
ax.plot(apple['Open'], label = "Apple")
ax.legend()
plt.show()

# 답지
# 여기서부터 코드 작성



# 코드 문제 7
tips = sns.load_dataset("tips")

# 답지
# 여기서부터 코드 작성

# 코드 문제 8
apple = yf.download("AAPL", start="2024-05-01", end="2024-09-30")

# 답지
# 여기서부터 코드 작성