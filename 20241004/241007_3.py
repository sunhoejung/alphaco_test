# 정규분포를 이루는 데이터
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import probplot
from scipy.stats import shapiro
from scipy import stats

np.random.seed(42)
normal_data = np.random.normal(size=100)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

probplot(normal_data, dist="norm", plot = axes[0])
sns.histplot(normal_data, axes=axes[1])

titles = ['QQ plot', 'Histogram']
for i, ax in enumerate(axes):
    ax.spines[['right', 'top']].set_visible(False)
    ax.set_title(titles[i])

plt.show()
shapiro(normal_data)

# 샤피로(shapiro) 윌크 검정
#데이터가 30개 미만이라는 가정 하에 정규성 검정 시행 (굳이 할 필요 없음)

tips = sns.load_dataset("tips")

smoker_yes = tips.loc[tips['smoker'] == 'Yes', :]
smoker_no = tips.loc[tips['smoker'] == 'No', :]



np.random.seed(42)
normal_data = smoker_yes['tip']

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

probplot(normal_data, dist="norm", plot = axes[0])
sns.histplot(normal_data, axes=axes[1])

titles = ['QQ plot', 'Histogram']
for i, ax in enumerate(axes):
    ax.spines[['right', 'top']].set_visible(False)
    ax.set_title(titles[i])

plt.show()
print(shapiro(normal_data))

# 등분산성 검증
t,p = stats.levene(smoker_yes['tip'], smoker_no['tip'])
print(t,p)

# 결론: p가 0.88, 귀무가설 채택, 두 그룹의 분산은 같다

t_stat, p_val = stats.ttest_ind(smoker_yes['tip'], smoker_no['tip'], equal_var = True)

print(f'T-statistic: {t_stat}')
print(f'P-value: {p_val}')