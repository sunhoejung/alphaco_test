# Candlestick Charts

import yfinance as yf
import plotly.graph_objects as go

indo = yf.download("INDO", start = "2023-01-01", end = "2024-09-30")

print(indo.head())

df = indo.reset_index()  #indo의 index는 Date. 아래 차트 넣기 위해 Date column으로 빼기

print(df.info())


fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.update_layout(
    title_text='Indonesia Energy',   #차트 제목, x축, y축 이름 설정
    title_x = 0.5,
    xaxis_title='Date',
    yaxis_title='Price',
    plot_bgcolor='lightgray',  # 차트 배경색
    paper_bgcolor='white',  # 전체 영역 배경색
    hovermode='x',  #hover
    xaxis_rangeslider_visible=True,  #슬라이드 기능
    xaxis_rangeslider_thickness=0.1    #슬라이드 두께 설정
) 

fig.update_traces(
    increasing_fillcolor='red',  # 상승일 때 캔들 몸통 색
    decreasing_fillcolor='blue',    # 하락일 때 캔들 몸통 색
    increasing_line_color='red',  # 상승일 때 테두리 색
    decreasing_line_color='blue'    # 하락일 때 테두리 색
)

fig.show()
