import numpy as np

arr = np.arange(8).reshape(4,2)
print(arr)

print(arr.sum())   #28   // axis 디폴트 값 = None

print(arr.sum(axis=0))   #[12 16]  // x축 방향으로 데이터 합 구함

print(arr.sum(axis=1))   #[ 1  5  9 13]  // y축 방향으로 데이터 합 구함

# 무작위 랜덤 함수 만들기

np.random.randint(10)

np.random.seed(42)   #seed 주면 아래 random숫자 안바뀜 (안에 아무 숫자 넣어도 됨)  // 머신러닝에서 사용
np.random.randint(10)

np.random.randint(45, size=6)  #0~45중 숫자 6개

np.random.randint(46, size=(3,4))   #0~45중 랜덤으로 3x4배열 채움

# 범위 주어지고 균등하게 분할 (시작값,종료값,분할지점)
x = np.linspace(0,99,10)
print(x)  #[ 0. 11. 22. 33. 44. 55. 66. 77. 88. 99.]
