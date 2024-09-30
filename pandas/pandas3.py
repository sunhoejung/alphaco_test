import pandas as pd
import random
import string


# Regenerating the dictionary where each key (종목코드, 종목명, 현재가, 등락률) has a list of values

data_dict = {
    "종목코드": [],
    "종목명": [],
    "현재가": [],
    "등락률": []
}

# Function to generate simpler 종목코드 and 종목명 ensuring the 종목코드 starts with '0'
def generate_code_name_for_dict(existing_codes):
    while True:
        code = '0' + ''.join(random.choices(string.digits, k=5))  # Ensure it starts with '0'
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # Simpler 종목명 with 2 letters
        if code not in existing_codes:
            return code, name

# Generating 10,000 rows of data
existing_codes_for_dict = set()

for _ in range(10000):
    code, name = generate_code_name_for_dict(existing_codes_for_dict)
    existing_codes_for_dict.add(code)
    current_price = random.randint(1000, 1000000)  # Simpler current price
    change_rate = round(random.uniform(-5, 5), 2)  # Simpler change rate
    
    data_dict["종목코드"].append(code)
    data_dict["종목명"].append(name)
    data_dict["현재가"].append(current_price)
    data_dict["등락률"].append(change_rate)

# Previewing a portion of the dictionary
data_dict_preview = {k: data_dict[k][:10] for k in data_dict}

sample_df= pd.DataFrame(data_dict_preview)

print(sample_df)

print(sample_df.head(1))  #데이터 상단부터  // head(n) n개만큼 출력

print(sample_df.tail(1))  #데이터 하단부터  // tail(n) n개만큼 출력

print(sample_df.info())  #dtype, 메모리 등 출력  // numpy기반 자료형 참조

print(sample_df.describe())  #최소값, 중앙값 등 통계적 내용들 출력

