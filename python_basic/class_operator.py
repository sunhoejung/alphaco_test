class A:
    def __init__(self, value):
        self.value = value

    #연산자 오버로딩
    def __add__(self, other):
        result = self.value + other.value
        return A(result)


a1 = A(2)
a2 = A(3)

a3 = a1 + a2    #6-8 코드 없으면 출력안됨
print(a3.value)

#즉, 클래스끼리 연산하는 경우 연산자 오버로딩이 필요하다