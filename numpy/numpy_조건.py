# 조건 연산
# 원하는 결과값: True/False

import numpy as np

arr = np.array([10,20,30])
print(arr>10)    #[False  True  True]

arr = np.array([10,20,30])
cond = [False, True, True]
print(arr[cond])   #arr에 cond 대입하면 true값만 나옴  '필터조건'

#라인 6~11 // 조건 주고 true값만 찾아서 그 값만 가져올 수 있음

#ex1
people_age = np.array([18,20,50,30,16])
can_drink = people_age > 18
print(people_age[can_drink])   #[20 50 30]

#ex2
people_age = np.array([18,20,50,30,16])
print(people_age[people_age > 18])  #ex1과 같은 결과. 즉, [] 안에 조건 바로 적어줄 수 있음

#ex3  다중 조건
people_age = np.array([18,20,50,30,16,65,70])
con0 = people_age > 18
con1 = people_age < 65

print(people_age[(con0 & con1)])   #[20 50 30] // and & or | not ~ 다 가능
#다중조건일 때 소괄호 주는게 좋음 // 이유: pandas 다중조건 필터링할 때는 소괄호 있어야만 가능


# np.where
a = np.arange(10)
print(a)
b = np.where(a<5,a,10*a)   #(if,a,else) -> 조건문
print(b)