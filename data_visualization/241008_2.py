from matplotlib import pyplot as plt
import seaborn as sns

# 회귀 모델 만들기

import statsmodels.api as sm


tips = sns.load_dataset("tips")

X = tips['total_bill']
y = tips['tip']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.summary())

# 회귀식 가정 검토

# 잔차의 정규성
# 귀무가설: 주어진 데이터는 정규분포를 이룬다
# 대립가설: 주어진 데이터는 정규분포를 이루고 있지 않다

from scipy import stats
from scipy.stats import shapiro
from scipy.stats import probplot
from scipy.stats import levene

res = model.resid
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

probplot(res, dist="norm", plot = axes[0]);
sns.histplot(res, axes=axes[1]);

titles = ['QQ plot', 'Histogram']
for i, ax in enumerate(axes):
    ax.spines[['right', 'top']].set_visible(False)
    ax.set_title(titles[i])

plt.show()
print(shapiro(res))

# 잔차의 등분산성
# 등분산성이 아니라면
# +종속 변수의 이상치 제거
# +변수의 로그변환

from statsmodels.stats.diagnostic import het_white
from statsmodels.compat import lzip

X = tips['total_bill']
y = tips['tip']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

predictions = model.predict(X)
residuals = y - predictions

plt.scatter(predictions, residuals)
plt.axhline(0, linestyle='--', color='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted Values')
plt.show()

# Optionally, use Levene's test to statistically test homoscedasticity
stat, p = levene(y, predictions)
print("'Levene's Test p-value:", p)

#The test
white_test = het_white(model.resid,  model.model.exog)

#Zipping the array with labels
names = ['Lagrange multiplier statistic', 'p-value','f-value', 'f p-value']
lzip(names,white_test)





iris = sns.load_dataset("iris")

X = iris['petal_length']
y = iris['sepal_length']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

predictions = model.predict(X)
residuals = y - predictions

plt.scatter(predictions, residuals)
plt.axhline(0, linestyle='--', color='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted Values')
plt.show()

# Optionally, use Levene's test to statistically test homoscedasticity
stat, p = levene(y, predictions)
print("'Levene's Test p-value:", p)

#The test
white_test = het_white(model.resid,  model.model.exog)

#Zipping the array with labels
names = ['Lagrange multiplier statistic', 'p-value','f-value', 'f p-value']
lzip(names,white_test)

# 로그 변환

import numpy as np

Q1 = tips['tip'].quantile(0.25)
Q3 = tips['tip'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_tips_sample = tips[(tips['tip'] >= lower_bound) & (tips['tip'] <= upper_bound)]

X = filtered_tips_sample['total_bill']
y = np.log(filtered_tips_sample['tip'])  #로그변환

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

predictions = model.predict(X)
residuals = y - predictions

plt.scatter(predictions, residuals)
plt.axhline(0, linestyle='--', color='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted Values')
plt.show()

white_test = het_white(model.resid,  model.model.exog)
names = ['Lagrange multiplier statistic', 'p-value','f-value', 'f p-value']
lzip(names, white_test)

# 다중 선형 회귀

import statsmodels.formula.api as smf

          # 종속변수     # 독립변수     독립변수
formula = "sepal_length ~ sepal_width + petal_length"
model = smf.ols(formula, data = iris).fit()
print(model.summary())
