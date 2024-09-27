import numpy as np

print(np.__version__)
# help(np)

num1 = [1,2,3]
num2 = [4,5,6]
# 더하면 원하는 값 [5,7,9]
# 근데 num1 + num2 하면 [1,2,3,4,5,6]
# 원하는 값 나오게 하려면 반복문 써야함. 즉, 연산시간 길어짐. numpy가 이를 해결해줌

num1_arr = np.array(num1)
num2_arr = np.array(num2)
print(num1_arr + num2_arr)  # = [5,7,9] (배열로 바꿔줌)

print(type(num1_arr))  # <class 'numpy.ndarray'>  자료형이 다름

num = [[1,2,3],[4,5,6],[7,8,9]]
num_arr = np.array(num)
# 자주 사용하는 특성&메소드
num_arr.shape  #tuple of array dimensions
num_arr.ndim  #number of array dimensions
num_arr.dtype  #데이터 저장 공간 크기 // 초기에 배열 만들 때 argument로 크기 지정 가능
num_arr.max()  #배열 전체에서 최대값 반환
num_arr.max(axis=0)  #각 열에서 최대값 반환  [7 8 9]
num_arr.max(axis=1)  #각 행에서 최대값 반환  [3 6 9]

# numpy 배열 만드는 방법
# 기본적으로는 다른 데이터 자료형을 numpy 배열로 변환
# 배열 생성도 가능
print(np.ones(3))  #ones는 1 세 개 배열 생성 [1.1.1.] 
print(np.zeros(3))  #zeros는 0 세 개 배열 생성 [0.0.0.]
print(np.ndarray(shape=(2,2,2)))   #n차원 배열 생성
# 배열의 차원 변경
temp_arr = np.arange(16)    # 1차원 배열 생성  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(temp_arr.reshape(2,8))   #2*8=16  [[ 0  1  2  3  4  5  6  7]  [ 8  9 10 11 12 13 14 15]]
print(temp_arr.reshape(2,2,4))  #2*2*4=16  [[[ 0  1  2  3]  [ 4  5  6  7]] [[ 8  9 10 11]  [12 13 14 15]]]

# dtype(비트) 중요
a16 = np.array([1.333333], dtype = np.float16)
a32 = np.array([1.333333], dtype = np.float32)
print(a16)  #[1.333]
print(a32)  #[1.333333]

# 수치 연산하다 오류 나오는 경우
arr = np.array([-1,22,-3])
print(arr/0)   #RuntimeWarning: divide by zero encountered in divide  [-inf inf -inf]  infinite

# 결측치 (Missing Values, 잃어버린 값), nan(Not a Number) 아직 정의되지 않은 숫자 의미
print(np.nan, type(np.nan))  #nan <class 'float'>
print(np.inf, type(np.inf))  #inf <class 'float'>
arr = np.array([-1,2,3])
print(arr + np.nan, type(arr + np.nan))  #[nan nan nan] <class 'numpy.ndarray'>
print(arr + np.inf, type(arr + np.inf))  #[inf inf inf] <class 'numpy.ndarray'>

# 인덱싱, 슬라이싱
arr= np.arange(10)  #[0 1 2 3 4 5 6 7 8 9]
print(arr[1:4])   #[1 2 3]

arr = np.arange(10).reshape(2,5)  #[[0 1 2 3 4] [5 6 7 8 9]]
arr[0]  #[0 1 2 3 4]
arr[0][2:4]   #[2 3]

arr = np.arange(10000).reshape(100,100)  #복잡함
print(arr[0:4,4])  #[  4 104 204 304]

arr = np.arange(20).reshape(4,5)
print(arr[1:,2:])  #[[ 7  8  9] [12 13 14] [17 18 19]]

