class Car():

    #클래스 변수
    instance_count = 0  #클래스 변수 생성 및 초기화

    def __init__(self, size, color):
        self.size = size    #인스턴스 변수 생성 및 초기화
        self.color = color    #인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1  #클래스 변수 이용하는 방법
        print(f"자동차 객체의 수: {Car.instance_count}")

    def move(self):
        print(f"자동차 {self.size}, {self.color}가 움직입니다.")

car1 = Car('small', 'white')
car2 = Car('big', 'gray')
car3 = Car('medium', 'black')

car1.move()
car2.move()
car3.move()