import pandas as pd
import os

data = {
    "종목명": ["3R", "3SOFT", "ACTS"],
    "현재가": [1510, 1790, 1185],
    "등락률": [7.36, 1.65, 1.28],
}

df = pd.DataFrame(data, index=["037730", "036360", "005760"])

print(df.head(1))

if not os.path.isdir("make_dir"):  #경로에 abc란 폴더 없다면
    os.mkdir("make_dir")  # 폴더 생성

df.to_csv("make_dir/data.csv")

