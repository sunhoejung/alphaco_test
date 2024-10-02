'''
plotly express
-high level interface
-graph objects에 비해 쉽지만 세밀한 커스터마이징은 안됨
'''

import plotly.express as px  #seaborn과 개념적으로 유사

iris = px.data.iris()
print(iris.head())

fig = px.scatter(iris, x = 'sepal_length', y = 'sepal_width')

fig.show()