class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, met_person_age):
        if met_person_age>self.age:
            print("안녕하세요")
        else:
            print("안녕")

person1 = Person("J", 28)
person1.greet(30)
person1.greet(18)