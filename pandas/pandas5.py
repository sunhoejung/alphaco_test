# 데이터 내보내기
import pandas as pd
import seaborn as sns
import openpyxl as xl

iris = sns.load_dataset("iris")

iris.to_csv("iris_240930.csv", index=False)  #index False로 안하면 index 하나의 column으로 나옴

# 데이터 파일 불러오기
df = pd.read_csv("iris_240930.csv")
print(df.head(1))

# 엑셀로 내보내기
iris.to_excel("iris_excel_240930.xlsx", index=False)  #엑셀은 openpyxl 설치 필요

# 엑셀 불러오기
excel_df = pd.read_excel("iris_excel_240930.xlsx")
print(excel_df)

# 주의! 경로 잘 확인해야함  cf)상위 폴더: 파일명 앞 ../


