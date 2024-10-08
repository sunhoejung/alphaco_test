import pandas as pd
import openpyxl

data = {
    "종목명": ["3R", "3SOFT", "ACTS"],
    "현재가": [1510, 1790, 1185],
    "등락률": [7.36, 1.65, 1.28],
}

df = pd.DataFrame(data, index=["037730", "036360", "005760"])

print(df.head(1))

df.to_csv("data_visualization/abc/df_csv_20241004.csv", index=False)

df.to_excel("data_visualization/abc/df_excel_20241004.xlsx", index=False)