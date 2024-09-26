from math import pi

#상위 클래스 (모양)
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass           #부모클래스에서 pass로 두고 자식에서 세분화, 처리할 수 있게 -> 오버라이딩

    def fact(self):
        return "2차원 도형이다"
    
#하위 클래스 (사각형)
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")   #self.name이 자동으로 생성됨 (부모 클래스의 생성자 호출)
        self.length = length

    def area(self):
        return self.length ** 2



#하위 클래스 (원)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(4)
print(a.area())
print(b.area())
