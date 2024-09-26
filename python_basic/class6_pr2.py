class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def get_description(self):
        return f"'{self.title}' (저자: {self.author}, 총 {self.pages}페이지)"
        
    def read(self, pages):
        if self.current_page + pages <= self.pages:
            self.current_page += pages
            print(f"{pages}페이지를 읽었습니다. 현재 {self.current_page}페이지에 있습니다.")
        else:
            print(f"책의 총 페이지 수를 초과할 수 없습니다!")

    def book_progress(self):
        print(f"이 책은 총 {self.pages}페이지이며, 현재 {self.current_page}페이지를 읽었습니다.")

book1 = Book('A', 'evan', 300)
book1.get_description()

