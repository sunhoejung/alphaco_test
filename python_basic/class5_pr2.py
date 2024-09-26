class Car:
    # __init__ 메서드: 객체가 생성될 때 호출되며 속성을 초기화합니다.
    def __init__(self, make, model, year):
        self.make = make  # 자동차 제조사
        self.model = model  # 자동차 모델
        self.year = year  # 제조 연도
        self.kilometer_reading = 0  # 주행 거리 (초기값 0)

    # 자동차의 전체 설명을 반환하는 메서드
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    # 현재 주행 거리 출력하는 메서드
    def read_kilometer(self):
        print(f"이 자동차의 현재 주행 거리는 {self.kilometer_reading} 킬로미터입니다.")
    
    # 주행거리 업데이트
    # 새로운 값이 기존 값보다 클 경우에만 업데이트
    def update_kilometer(self, kilometers):
        if kilometers >= self.kilometer_reading:
            self.kilometer_reading = kilometers
            print(f"업데이트 확인 : {self.kilometer_reading} 킬로미터")
        else:
            print(f"현재 : {self.kilometer_reading}, 다시 입력해주세용") 

    # 주행 거리를 증가시키는 메서드
    def increment_kilometer(self, kilometers):
        if kilometers > 0:
            self.kilometer_reading += kilometers
        else:
            print("음수가 입력되었습니다. 양수로 입력해주세요")

my_car = Car("현대", "아반떼", 2024)
description = my_car.get_description()
print(description)
my_car.read_kilometer()
my_car.increment_kilometer(100)
my_car.read_kilometer()