class Spaceship:
    def __init__(self, color, speed, passengers):
        self.color = color
        self.speed = speed
        self.passengers = passengers

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed

    def get_passengers(self):
        return self.passengers
    
    def set_passengers(self, passengers):
        self.passengers = passengers

    def add_passenger(self, plus_passenger):
        self.passengers += plus_passenger

    def remove_passenger(self, minus_passenger):
        if minus_passenger >= self.passengers:
            print("탑승 인원 수가 0명 이하로 내려갈 수 없습니다")
        else:
            self.passengers += minus_passenger

    def increase_speed(self, amount):
        self.speed += amount

    def decrease_speed(self, amount):
        if amount >= self.speed:
            print("속도가 0 이하로 내려갈 수 없습니다")
        else:
            self.speed -= amount

    def get_info(self):
        return f"색상: {self.color} 속도: {self.speed} 탑승인원: {self.passengers}"




def simulate_spaceship():
    spaceship = Spaceship("Red", 10000, 5)
    
    while True:
        print("\n현재 우주선 상태:")
        print(spaceship.get_info())
        
        print("\n무엇을 하시겠습니까?")
        print("1. 색상 설정")
        print("2. 속도 증가")
        print("3. 속도 감소")
        print("4. 탑승인원 추가")
        print("5. 탑승인원 하차")
        print("6. 시뮬레이션 종료")
        
        choice = input("선택을 입력하세요 (1-6): ")

        if choice == '1':
            color = input("새 색상을 입력하세요: ")
            spaceship.set_color(color)
            print(f"색상이 {color}(으)로 변경되었습니다")
        
        elif choice == '2':
            amount = int(input("속도를 얼마나 증가시키겠습니까?: "))
            spaceship.increase_speed(amount)
        
        elif choice == '3':
            amount = int(input("속도를 얼마나 감소시키겠습니까?: "))
            spaceship.decrease_speed(amount)
        
        elif choice == '4':
            number = int(input("추가할 탑승인원 수를 입력하세요: "))
            spaceship.add_passenger(number)
        
        elif choice == '5':
            number = int(input("하차할 탑승인원 수를 입력하세요: "))
            spaceship.remove_passenger(number)
        
        elif choice == '6':
            print("시뮬레이션을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다. 1에서 6 사이의 숫자를 입력하세요.")

# 시뮬레이션 실행
simulate_spaceship()