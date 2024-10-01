import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

estate = pd.read_csv("seoul_real_estate.csv")

print(estate.loc[estate['BLDG_AREA']>=900,:])  #900이상이 적절한지 양 확인 (추출 기준 잡기 위해)
highest_values = estate['BLDG_AREA'] >= 900

print(estate['BLDG_AREA'][highest_values])

print(estate['OBJ_AMT'][highest_values])

fig, ax = plt.subplots()
ax.scatter(estate['BLDG_AREA'], estate['OBJ_AMT'], alpha=0.5)
ax.scatter(estate['BLDG_AREA'][highest_values], estate['OBJ_AMT'][highest_values], color = 'red')  #조건에 해당되는 부분만 빨간색으로 표시
plt.show()