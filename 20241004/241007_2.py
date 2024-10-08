import pandas as pd
import numpy as py
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

print(tips['sex'].value_counts())

# 데이터 분리 작업 선행
smoker = tips.loc[tips['smoker']=='Yes', :]
print(smoker)

non_smoker = tips.loc[tips['smoker']=='No', :]


fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(15,5))

sns.histplot(smoker['tip'], ax = ax[0])

sns.histplot(non_smoker['tip'], ax = ax[1])

plt.show()
