'''
plotly: 대화형 차트

graph_objects
-low level interface : 아래부터 쌓아가야 함 / 구성품도 내가 만들어야 함
-세밀하게 커스터마이징 가능
'''
'''
cf) matplotlib & seaborn : 연구자, academic, 보고서 작성이 잦은 사람들에게 좋음
    flotly: 웹개발 도구 / 개발자 커리어 입문용
    tableau, powerBI : 솔루션 / 배워도 회사에서 안쓰면 무용지물 / 기본값이 되면 안됨
'''



import pandas as pd
import plotly.graph_objects as go #matplotlib과 개념 유사

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = pd.DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)
print(df)

fig = go.Figure()  #그래프 그리기 위한 객체 생성
fig.add_trace(go.Bar(x=[1,2,3],y=[1,5,3]))  #막대그래프 생성

fig.show()