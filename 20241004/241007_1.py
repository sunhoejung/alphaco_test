import pandas as pd
import numpy as np
from scipy.stats import ttest_rel

df = pd.read_csv("insectsprays.csv")

print(df.head())

sample_mean = df['before_spr'].mean()

print(sample_mean)

df['diff'] = df['before_spr'] - df['after_spr']

sample_mean_diff = df['diff'].mean()

print('차이의 표본 평균: ', round(sample_mean_diff,2))

t_stat, p_value = ttest_rel(df['before_spr'], df['after_spr'])

print("검정 통계량: ", round(t_stat, 2))
print("p 값: ", round(p_value, 4))

