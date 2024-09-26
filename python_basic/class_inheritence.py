class 상위클래스:
    pass

class 하위클래스(상위클래스):
    pass

class 동물:

    name = ""

    def 음식먹기(self):
        print("저는 음식을 먹습니다")

동물1 = 동물()
동물1.음식먹기()

class 강아지(동물):

    def 자기소개(self):
        print(f'내 이름은 {self.name}')

강아지1 = 강아지()
강아지1.name = "뽀삐"
강아지1.음식먹기()
강아지1.자기소개()
'''
상속은 is-a 관계

Car is a vehicle ==> 상위 클래스 : vehicle, 하위 클래스 : Car
Apple is a fruit ==> 상위 클래스 : fruit, 하위 클래스 : Apple
Cat is an animal ==> 상위 클래스 : animal, 하위 클래스 : Cat

관계를 잘 설정하기

'''