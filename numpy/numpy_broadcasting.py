# numpy.broadcast
# 배열의 사이즈가 다르더라도 연산을 할 수 있게 지원

import numpy as np

a = np.array([1,2,3])
b = np.array([1,2,3])
a + b  #[2 4 6]

a = np.array([1,2,3])
b = 3.0 #배열이 달라도 연산하면 3.0의 값을 가지고 있는 배열로 만들어줌
a + b  #[4. 5. 6.]