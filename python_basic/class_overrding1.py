'''
클래스 설계 하다보면 부딪히는 흔한 문제
==> 메소드 명이 같을 때
해결책: 오버라이딩(=자식 클래스가 해당 메소드의 개념을 재정의), 다형성
'''

#부모 클래스
class 동물:
    def 울음소리(self):
        return "동물 울음소리"
    
#자식 클래스
class 강아지(동물):
    def 울음소리(self):
        return "멍멍"
    
class 고양이(동물):
    def 울음소리(self):
        return "야옹"
    
def make_sound(animal):
    print(animal.울음소리())


#객체 생성
dog = 강아지()
cat = 고양이()
#dog.울음소리()
#cat.울음소리()


make_sound(dog)
make_sound(cat)