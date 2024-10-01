# matplotlib 기본 문법
import matplotlib.pyplot as plt

# Prepare the data
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(10,6))   # fig, axes 객체 생성  / nrows: 행 / ncols: 열 / 그림 사이즈=(width, height)
# 사이즈에 맞는 그래프 생성됨
# 보통 fig는 거의 안 건드리고 ax만 건드림 / artist layer

# cf) matplotlib 자료형 리스트, 즉 dataframe은 리스트로 변환해줘야 함
ax.plot(dates, min_temperature, label = "Min Temp")
ax.plot(dates, max_temperature, label = "Max Temp")
ax.legend()

plt.show()  #그림 보여줌

print(fig)  #Figure(1250x750)
print(ax)  #Axes(0.125,0.11;0.775x0.77)

