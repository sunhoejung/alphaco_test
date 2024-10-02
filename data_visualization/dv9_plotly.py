# plotly 기본 옵션

import plotly.express as px
import plotly.graph_objects as go

iris = px.data.iris()
print(iris.head())

fig = px.scatter(iris, x = 'sepal_length', y = 'sepal_width', color = 'species')

fig.add_trace(  #add_trace: 객체 위에다 추가로 그린다는 의미
    go.Scatter(  #산점도 아님
        x = [4.5, 7.5],  #x축 범위 설정
        y = [4, 2],  #y축 범위 설정
        mode = "lines",  #line 차트
        line = go.scatter.Line(color = "red"),
        showlegend = False
    )
)
fig.show()

fig = px.scatter(iris, x = 'sepal_length', y = 'sepal_width', color = 'species')

fig.add_trace(
    go.Scatter(  #산점도 아님
        x = [4.5, 7.5],  #x축 범위 설정
        y = [4, 2],  #y축 범위 설정
        mode = "markers",  #점 표시
        marker = dict(size = 20, color = "red"),  #json) dict 사용
        showlegend = False
    )
)

fig.show()