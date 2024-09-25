#1
print("문제1")
a = 10
b = 5.5
c = a + b
print(type(c))

#2
print("문제2")
print("문자열 '100'과 정수 50은 타입이 달라서 더하기 불가")
print("해결방법: 문자열 100을 int를 통해 형변환한 후 더하기")

#3
print("문제3")
print("리스트와 튜플은 더할 수 없다")

#4
print("문제4")
x = None
y = str(x)
print(y)
print("문자열로 가능")

#5
print("문제5")
a5 = 3
b5 = float(a5)
print("%.1f" %b5)

#6
print("문제6")
s = "Hello"
s3 = "hello" * 3
print(type(s3))

#7
print("문제7")
x7 = 7
y7 = str(x7)
z7 = y7 + "3"
print(z7)

#8
print("문제8")
a8 = True
b8 = False
c8 = a8 + b8
print(c8, type(c8))

#9
print("문제9")
a9 = 25
sub_a9 = a9 / 0.5
print(sub_a9, type(sub_a9))

#10
print("문제10")
text = "12345"
int_text = int(text)
res10 = int_text + 10
print(res10)

#11
print("문제11")
l11 = [10,20,30,40,50]
a = 0
for i in l11:
    if a < i:
        a = i
print(a)

#12
print("문제12")
l12 = [1,2,3,4,5]
sum = 0
for i in l12:
    sum += i
print(sum)

#13
print("문제13")
t13 = (5,10,15,20)
print(t13[1])

#14
print("문제14")
t14_1 = (1,2,3)
t14_2 = (4,5,6)
l14_1 = list(t14_1)
l14_2 = list(t14_2)
res_list = l14_1 + l14_2
print(tuple(res_list))

#15
print("문제15")
d14 = {'a':1, 'b':2, 'c':3}
d14['b'] = 10
print(d14)

#16
print("문제16")
d16 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(d16.keys())

#17
print("문제17")
i = 1
while i < 6:
    print(i)
    i+=1

#18
print("문제18")
i = 10
while i < 1:
    print(i)
    i-=1

#19
print("문제19")
l19 = [2,4,6,8,10]
res_list = [2*i for i in l19]
print(res_list)

#20
print("문제20")
t20 = "Python"
for i in range(len(t20)):
    print(t20[i])