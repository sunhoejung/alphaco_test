class Bicycle():        #클래스를 만들 때는 클래스명 특성과 행동을 정의하는 것이 핵심 포인트
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
    
    def move(self, speed):
        print(f"자전거 : 시속 {speed} 킬로미터로 전진")

    def stop(self):
        print(f"{self.wheel_size}, {self.color}의 특성을 가진 자전거 정지하세요")
    

my_bicycle = Bicycle(26, 'black')
print(my_bicycle.wheel_size, my_bicycle.color)
my_bicycle.move(30)
my_bicycle.stop()