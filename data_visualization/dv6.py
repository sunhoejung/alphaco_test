# matplotlib 옵션 설정
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, FuncFormatter
import seaborn as sns
import numpy as np

tips = sns.load_dataset("tips")  #팁 준 사람들 정보
print(tips.head(1))
print(tips.info())  #(dtype)category: 범주형 데이터셋

group_mean = tips.groupby(['day'])['total_bill'].agg("mean")  #day  (line 64)
#print(group_mean)
h_day = group_mean.sort_values(ascending=False).index[0]  #내림차순
h_mean = np.round(group_mean.sort_values(ascending=False)[0], 2)   #가장 높은 숫자(요기선 일요일) round  // 아래 일요일 색상 강조 위해 설정
#print(h_day)
#print(h_mean)

# 왼쪽 그래프

fig,ax = plt.subplots(nrows=1, ncols=2, figsize=(16,5))
sns.barplot(tips, x='day', y='total_bill', errorbar=None, color='lightgray', alpha=0.85, zorder=2, ax=ax[0])  #errorbar 삭제


# 막대 그래프 위에 값 표시하기
for p in ax[0].patches:        #p: 막대그래프의 막대, 하나의 인스턴스(Rectangle)
    print(p)
    print(type(p))
    '''
Rectangle(xy=(-0.4, 0), width=0.8, height=17.6827, angle=0)
<class 'matplotlib.patches.Rectangle'>
Rectangle(xy=(0.6, 0), width=0.8, height=17.1516, angle=0)
<class 'matplotlib.patches.Rectangle'>
Rectangle(xy=(1.6, 0), width=0.8, height=20.4414, angle=0)
<class 'matplotlib.patches.Rectangle'>
Rectangle(xy=(2.6, 0), width=0.8, height=21.41, angle=0)
<class 'matplotlib.patches.Rectangle'>
'''
#자동으로 요일별 평균이 나오는 걸 알 수 있음
    print(p.get_height())  #get_height통해 원하는 값 받음
    print(p.get_width())
    height = np.round(p.get_height(),2)  #숫자 깔끔히 하기 위해 round
    ax[0].text(p.get_x() + p.get_width()/2, height+1, height, ha='center', size=12)   #각 막대 위에 글자 올라감
    #                   get_x                                                             height+1                         height
    #text(막대 위 글자의 x축 위치(width/2 더해서 가운데로/처음 위치는 각 막대 시작부분), height+1 통해 막대 위에 위치 하게, 실제 값(높이 값))


#옵션
ax[0].set_title("Just Bar Graph", size=16)
ax[0].set_ylim(-0.5, 25)  #막대 위 숫자 표 안에 들어오게 y축 설정




# 오른쪽 그래프

sns.barplot(tips, x='day', y='total_bill', errorbar=None, color='lightgray', alpha=0.85, zorder=2, ax=ax[1])  


for p in ax[1].patches:
    height = np.round(p.get_height(),2)

    fontweight = "normal"
    color = 'k'
    if h_mean == height:   #평균 bill 제일 높은 sunday 조건에 걸림
        fontweight = "bold"
        color = "darkred"
        p.set_facecolor(color)
        p.set_edgecolor("black")   

    ax[1].text(p.get_x() + p.get_width()/2, height + 1, height, ha = 'center', size=12, fontweight=fontweight, color=color)

ax[1].set_title("Ideal Bar Graph", size=16)
ax[1].set_ylim(-0.5, 25)

# spines 항목 정리
ax[1].spines['top'].set_visible(False)  #테두리 윗선이 사라짐
ax[1].spines['left'].set_visible(False)  #테두리 왼쪽선이 사라짐
ax[1].spines['right'].set_visible(False)  #테두리 오른쪽선이 사라짐

ax[1].spines['left'].set_position(("outward", 20))  #좌측에 공간 여백 만들기

# y축 정리
def major_formatter(x, pos):    #소수점 2번째자리 + $ => y축 문자 포매팅
    return "%.2f$" % x

formatter = FuncFormatter(major_formatter)

ax[1].yaxis.set_major_locator(MultipleLocator(10))   #y축의 큰 눈금 간격 10단위로
ax[1].yaxis.set_major_formatter(formatter)   #20.00$와 같이 출력
ax[1].yaxis.set_minor_locator(MultipleLocator(5))   #y축의 작은 눈금 간격 10단위로

# 축 라벨 지정
ax[1].set_ylabel("Avg Bill($)", fontsize=10)
ax[1].set_xlabel("Date", fontsize=10)

ax[1].grid(axis="y", which="major", color="lightgray")
ax[1].grid(axis="y", which="minor", ls=":")

plt.show()