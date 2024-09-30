import pandas as pd

df = pd.read_csv("../iris_240930.csv")  #../ : 상위폴더 접근
print(df.head(1))