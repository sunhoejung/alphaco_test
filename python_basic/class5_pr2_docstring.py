class Car:
    """
    Car 클래스는 자동차의 제조사, 모델, 연도, 주행 거리를 관리하는 클래스로,
    자동차에 대한 정보를 저장하고, 주행 거리 관련 기능을 제공합니다.
    """
    
    def __init__(self, make: str, model: str, year: int):
        """
        객체 초기화 메서드. 자동차의 제조사, 모델, 연도, 주행 거리를 설정합니다.

        Args:
            make (str): 자동차 제조사
            model (str): 자동차 모델
            year (int): 자동차 제조 연도
        """
        self.make = make  # 자동차 제조사
        self.model = model  # 자동차 모델
        self.year = year  # 제조 연도
        self.kilometer_reading = 0  # 주행 거리 (초기값 0)

    def get_description(self) -> str:
        """
        자동차의 전체 설명을 반환합니다.

        Returns:
            str: 자동차의 연도, 제조사, 모델을 문자열로 반환.
        """
        return f"{self.year} {self.make} {self.model}"

    def read_kilometer(self) -> None:
        """
        현재 주행 거리를 출력합니다.

        Returns:
            None
        """
        print(f"이 자동차의 현재 주행 거리는 {self.kilometer_reading} 킬로미터입니다.")
    
    def update_kilometer(self, kilometers: int) -> None:
        """
        주행 거리를 업데이트합니다. 입력된 주행 거리가 기존 주행 거리보다 큰 경우에만 업데이트됩니다.

        Args:
            kilometers (int): 새로운 주행 거리
            
        Returns:
            None
        """
        if kilometers >= self.kilometer_reading:
            self.kilometer_reading = kilometers
            print(f"업데이트 확인 : {self.kilometer_reading} 킬로미터")
        else:
            print(f"현재 : {self.kilometer_reading}, 다시 입력해주세용") 

    def increment_kilometer(self, kilometers: int) -> None:
        """
        입력한 만큼 주행 거리를 증가시킵니다. 음수가 입력되면 오류 메시지를 출력합니다.

        Args:
            kilometers (int): 증가시킬 주행 거리
            
        Returns:
            None
        """
        if kilometers > 0:
            self.kilometer_reading += kilometers
        else:
            print("음수가 입력되었습니다. 양수로 입력해주세요")


# 사용 예시
my_car = Car("현대", "아반떼", 2024)

# 자동차 설명 출력
description = my_car.get_description()
print(description)

# 주행 거리 확인
my_car.read_kilometer()

# 주행 거리 증가
my_car.increment_kilometer(100)

# 업데이트된 주행 거리 확인
my_car.read_kilometer()

print(my_car.__doc__)        #docstring 내용 출력
help(my_car)      #클래스 설명 도움