#yahoo api에서 무료 주식 데이터 가져오기
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")

fig, ax = plt.subplots()

# x축은 Date가 현재 시리즈 상에서 index로 되어 있음
ax.plot(data['Open'])  #plot 받아올 때 시리즈 형태  // date가 인덱스로 되어 있음 

plt.show()

data2 = data.copy()

data2 = data.reset_index()  #index를 변환  // date가 column으로.. index 아님  // 즉, 날짜로 나와야 하는데 x축이 숫자(인덱스)로 나옴
# 그래서 바로 data['Open']을 할지 처리를 해줄지 index와 x축 잘 판단해서 해야 함!

# data2 처리하려면 data3 = data2.set_index("Date")로 date로 인덱스 설정을 다시 해줌
data2.head(1)

fig,ax = plt.subplots()
ax.plot(data2['Open'])

plt.show()  #reset_index() 했기 때문에 x축 index로 나온다

# 예재 : 애플, 엔비디아 주식 두개 불러와서 동시에 라인 차트 그리기

data_aapl = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
data_nvda = yf.download("NVDA", start="2020-01-01", end = "2024-09-30")
data_intel = yf.download("INTC", start="2020-01-01", end = "2024-09-30")

fig, ax = plt.subplots()  #기본값 셋팅

ax.plot(data_aapl["Open"], label = "Apple")
ax.plot(data_nvda["Open"], label = "Nvidia")
ax.set_title("Stocks")  #이름 표시
ax.legend()  #label 표시

plt.show()

# 차트 분할  (1*3)

fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize=(10,4))  #1*3 형태로 차트 세 개 표시됨

ax[0].plot(data_aapl["Open"], label = "Apple")  
ax[1].plot(data_nvda["Open"], label = "Nvidia")  
ax[2].plot(data_intel["Open"], label = "Intel")  

ax[0].set_title("Apple")
ax[1].set_title("Nvidia")
ax[2].set_title("Intel")

ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

# 차트 분할  (2*2)

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize=(8,4))  #2*2 형태로 차트 네 개 표시됨

ax[0,0].plot(data_aapl["Open"], label = "Apple") 
ax[0,1].plot(data_nvda["Open"], label = "Nvidia") 
ax[1,0].plot(data_intel["Open"], label = "Intel")  

ax[0,0].set_title("Apple")
ax[0,1].set_title("Nvidia")
ax[1,0].set_title("Intel")

ax[0,0].legend()
ax[0,0].legend()
ax[0,0].legend()

fig.tight_layout()  #가려진 title 보이게 해줌
plt.savefig("myStocks.png")  #차트 이미지로 저장
plt.show()