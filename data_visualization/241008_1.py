# 상관분석
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

iris = sns.load_dataset("iris")
print(iris.head(1))

# 공분산 구하기

df = iris.loc[:9, ['sepal_width', 'petal_length']]
print(df)
sepal_w_mean = df['sepal_width'].mean()
petal_l_mean = df['petal_length'].mean()
print(sepal_w_mean, petal_l_mean)

df['sepal_diff'] = df['sepal_width'] - sepal_w_mean
df['petal_diff'] = df['petal_length'] - petal_l_mean
df['multiple'] = df['sepal_diff'] * df['petal_diff']
print("편차의 합:", df['multiple'].sum())
print("공분산 :", df['multiple'].sum()/(len(df)))

print(df.cov(ddof=0)) #ddof : 자유도

print(iris.iloc[:, :4].cov(ddof=0))



df['sepal_diff'] = df['sepal_width'] - sepal_w_mean
df['petal_diff'] = df['petal_length'] - petal_l_mean
df['multiple'] = df['sepal_diff'] * df['petal_diff']
df['sepal_squared'] = df['sepal_diff'] ** 2
df['petal_squared'] = df['petal_diff'] ** 2

cov_value = df['multiple'].sum()/(len(df))
sepal_squared_std = np.sqrt(np.mean(df['sepal_squared']))
petal_squared_std = np.sqrt(np.mean(df['petal_squared']))
print("편차의 합:", df['multiple'].sum())
print("공분산 :", cov_value)
print("sepal_squared 표준편차:", sepal_squared_std)
print("petal_squared 표준편차:", petal_squared_std)
print("상관계수:", cov_value / (sepal_squared_std * petal_squared_std))



# 상관계수 구하기

print(iris.iloc[:, :4].corr())

fig, ax = plt.subplots(ncols = 3, figsize=(16,5))

sns.scatterplot(iris, x = 'sepal_width', y = 'sepal_length', ax = ax[0])
sns.scatterplot(iris, x = 'petal_length', y = 'sepal_length', ax = ax[1])
sns.scatterplot(iris, x = 'petal_width', y = 'sepal_length', ax = ax[2])

plt.show()

