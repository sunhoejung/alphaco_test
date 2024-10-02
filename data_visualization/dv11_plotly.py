#hover 설정
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder().query("continent=='Oceania'")
print(df.head(5))

fig = px.line(df, x = 'year', y = 'lifeExp', color = 'country')

#그래프 내부의 색상, 모양 등을 변경 : update_traces()  cf)그래프 외부: update_layout()

fig.update_traces(mode="markers+lines")   #선에다 마커(원) 추가

fig.update_layout(hovermode='x')  #hover 설정 - x축에 뜬다


fig.show()



'''
모든 성질, 메소드 기억 못함
update_traces
update_layout
add_trace
세 개 기억하고 찾기
'''