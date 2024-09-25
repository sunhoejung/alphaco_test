class 책:
    title = None     #속성
    author = None     #속성
    pages = 0     #속성
    price = 0     #속성
    discount = 0     #속성

    def 읽는시간(self, reading_speed = 30):       #메소드
        return round(self.pages / reading_speed, 1)

# 클래스 만들었으니 인스턴스 생성
책01호 = 책()
print(책01호)

책02호 = 책()
print(책02호)

# 책01호, 책02호 출력값 둘 다 책으로 나옴 => 둘 다 class인 책을 참조하지만 주소가 다름 => 서로 다른 애들임

책01호.title = "Streamlit"
책01호.author = "Evan"
책01호.pages = 560
책01호.price = 40000
책01호.discount = 10


print(책01호.title)    # 이처럼 하면 하나하나 다 적어줘야함
책02호.TITLE = "Python"
print(책02호.TITLE)    # 이또한 출력이 되긴 함. but 안 좋은 방식


출력값 = 책01호.읽는시간()  # class 내 읽는 시간이라는 함수 호출
print(출력값)

# 위 코드는 비효율적

class 책1():
    def __init__(self, title, author, pages, price, discount=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.discount = discount

    def reading_time(self, reading_speed = 30):       #메소드
        return round(self.pages / reading_speed, 1)

    def apply_discount(self):
        return self.price*(1 - self.discount)


책1_01호 = 책1("샘플", "Evan", 300, 2000, 0.1)  # 위 코드보다 간결함
책1_02호 = 책1("샘플2", "J", 200, 1000, 0.2)
print(책1_01호.title)

print(책1_01호.reading_time(10))
print(int(책1_01호.apply_discount()))
