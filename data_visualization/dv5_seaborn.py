import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

data_aapl = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
data_nvda = yf.download("NVDA", start="2020-01-01", end = "2024-09-30")
data_intel = yf.download("INTC", start="2020-01-01", end = "2024-09-30")

apple2 = data_aapl.reset_index()
apple2.head(1)

# seaborn - matplotlib 매개해주는 것 : ax

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize=(10,4))  

ax[0,0].plot(data_aapl["Open"], label = "Apple")  
ax[0,1].plot(data_nvda["Open"], label = "Nvidia")  
ax[1,0].plot(data_intel["Open"], label = "Intel")  
sns.lineplot(data = apple2, x = 'Date', y = 'Open', ax = ax[1,1])    #ax로 seaborn & matplotlib 매개


ax[0,0].set_title("Apple")
ax[0,1].set_title("Nvidia")
ax[1,0].set_title("Intel")
ax[1,1].set_title("Apple from Seaborn stocks")

ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()

fig.tight_layout()

plt.show()