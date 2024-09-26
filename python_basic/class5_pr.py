"""
- Car 클래스를 만들어보겠습니다. 
- Car 클래스는 `__init__`, `get_description`, `read_kilometer`, `update_kilometer`, `increment_kilometer`라는 메서드를 갖습니다.
    + `__init__` 메서드는 클래스의 생성자로, 객체가 생성될 때 호출됩니다.
- 속성 사용하기
    + `self.make`, `self.model`, `self.year`, `self.kilometer_reading` 클래스의 속성입니다.
    + 객체가 생성될 때 속성값이 초기화됩니다.

- self의 의미
    + self는 클래스의 인스턴스를 참조합니다. 클래스 내의 메서드가 객체의 속성에 접근하거나 다른 메서드를 호출할 때 사용합니다.
    + self를 통해 클래스 내의 속성 및 메서드를 정의하고 접근할 수 있습니다.

- 클래스의 위치 인수, 키워드 인수
    + `__init__` 메서드의 make, model, year는 위치 인수로 전달됩니다.
    + 메서드를 호출할 때 my_car.update_kilometer(kilometers=500)처럼 키워드 인수로 사용할 수도 있습니다.
"""

class Car():
    def __init__(self, make, model, year, kilometer_reading=0):
        self.make = make   #자동차 회사
        self.model = model    #모델
        self.year = year    #연식
        self.kilometer_reading = kilometer_reading   #주행거리

    def get_description(self):
        print(f"이 차는 {self.make}회사 {self.model}모델 {self.year}연식입니다")    #자동차 설명

    def read_kilometer(self):
        print(f'이 차는 {self.kilometer_reading}km 주행했습니다')     #주행거리 표시

    def update_kilometer(self, plus_kilometer=0):
        print(f'이 차의 최신 주행거리는 {(self.kilometer_reading + plus_kilometer)}km입니다')       #최신 주행거리 표시

    
car1 = Car('Hyundai', 'G80', '2022', 20000)
car2 = Car('Kia', 'K5', '2018', 30000)
car3 = Car('Toyota', 'Camry', '2019', 50000)

car1.get_description()
car1.read_kilometer()
car1.update_kilometer(1000)

car2.get_description()
car2.read_kilometer()
car2.update_kilometer()

car3.get_description()
car3.read_kilometer()
car3.update_kilometer(5000)