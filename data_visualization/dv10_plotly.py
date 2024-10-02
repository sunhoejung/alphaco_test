# plotly 기본문법

import plotly.express as px
import plotly.graph_objects as go

# express 방식 <1>
fig = px.bar(x=["a","b","c"], y=[1,3,2], width=600, height=400,
             title = "타이틀 설정")
fig.show()

# graph_objects 방식 <2>
fig = go.Figure(data=[go.Bar(x=["a","b","c"], y=[1,3,2])],
                layout = go.Layout(title=go.layout.Title(text = "Title 설정"))   #title 설정법 but, 복잡
                )
# express와 달리 너비는 따로 설정해야 함
fig.update_layout(width=600,  #레이아웃: 그래프 외부
                height=400,
                margin_l = 50,  #좌측 여백
                margin_r = 30,  #우측 여백
                paper_bgcolor = "lightblue"  #백그라운드 색상 지정
                )
fig.show()

# express  <3>
fig = px.bar(x = ["a", "b", "c"], 
             y = [1, 3, 2], width = 600, height = 300)

fig.update_layout(title_text='타이틀 설정')  #비교적 간단한 제목 설정법

fig.show()

# graph_object  <4>
fig = go.Figure(data=[go.Bar(x = ["a", "b", "c"], y = [1, 3, 2])])

fig.update_layout(title_text='Title 설정')  #graph_object도 적용됨

fig.show()