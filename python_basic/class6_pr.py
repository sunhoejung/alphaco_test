class Book:
    def __init__(self, name, desc, total_page):
        self.name = name
        self.desc = desc
        self.total_page = total_page
        self.now_page = 0

    def print_desc(self):   #책 설명 출력
        print(f'선택하신 {self.name} 책은 {self.desc}입니다')

    def read_book(self, how_many_pages):      #읽은 페이지 만큼 기록&읽은 양 출력
        self.now_page += how_many_pages
        if how_many_pages > (self.total_page - self.now_page):
            print("읽을 페이지 수가 전체 페이지 수를 초과했습니다")
        else:
            print(f"{self.name} 책은 {self.now_page}쪽 만큼 읽었습니다")

book1 = Book("헨젤과그레텔", "동화", 200)
book2 = Book("홍길동전", "고전문학", 210)
book3 = Book("원피스", "만화", 100)

book1.print_desc()
book2.print_desc()
book3.print_desc()

book1.read_book(300)
book2.read_book(20)
book3.read_book(35)
    
book2.read_book(30)