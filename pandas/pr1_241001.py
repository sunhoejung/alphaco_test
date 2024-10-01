import pandas as pd

# 데이터프레임 생성
data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = pd.DataFrame(data=data, columns=columns)
df.info()

df["03/02"] = df["03/02"].map(lambda x:int(x.replace(',','')))   #column 일부분만 int형으로 바꾸기
print(df)