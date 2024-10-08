# 카이제곱 검정

import seaborn as sns

tips = sns.load_dataset("tips")

# 관측값

관측값 = tips['day'].value_counts().sort_index()
print(관측값)

# 기대값

기대값 = len(tips)/len(관측값)
print(기대값)

# 균등 분포 

기대값들 = [len(tips) / len(관측값)] * len(관측값)

# 적합도 검정 수행

from scipy import stats
x,p = stats.chisquare(f_obs=관측값, f_exp=기대값들)

print(x,p)

if p>0.05:
    print('관측된 데이터는 기대값 균등분포와 일치한다')
else:
    print('관측된 데이터는 기대값 균등분포와 일치하지 않는다')

# 독립성 검정
# tips data - 성별과 흡연 여부 : 성별에 따라 흡연 여부와 상관이 있는가

import pandas as pd

# 교차표 생성

c_table = pd.crosstab(tips['sex'], tips['smoker'])

print(c_table)

# 독립성 검정
t,p,dof,expected = stats.chi2_contingency(c_table)
print(f"Chi-square Statistic: {x}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

