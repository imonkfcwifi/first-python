print("hello world")

a= 3
b =2
c= a+b
print(c)

my_name = "roh"
print(my_name)

bool = True

def say_hello():
    print("h1")
# print가 say_hello 안에있음을 명시하는 빈 공백
say_hello()

def say_goodbye(name, age):
    print(name, "whatsup", age)
say_goodbye("imonkfcwifi",26)

# parameter = 밖에서 받을 데이터의 placeholder 역할 (넣을 공간 박스의 이름 name)
# parameter에 넣는 인자 (실제로 넣는데이터) = argmument(imonkfcwifi)

def say_goodbyeyo(name="anno"):
    print(name)
say_goodbyeyo()

def plus(a=0, b=0):
    print(a + b)

def minus(a=0, b=0):
    print(a - b)

def multiply(a=0, b=0):
    print(a * b)

def divide(a=0, b=1):
    print(a / b)

def power(a=0, b=1):
    print(a ** b)

# 함수에 필요한 모든 parameter들을 보내지 않는 경우를 관리한다.

def tax_value(money):
   return money

#    return 이란 함수 바깥으로 값을 보낸다는 의미

def pay(tax):
    print("your tax is :", tax)

# to_play = tax_value(3000000)
# pay(to_play)

pay(tax_value(30000000))

my_age = 12
my_ha = "ha"

print(f"my name is {my_ha}, my age is {my_age}")
# string 안에 변수넣는법 -> f""

def juice_maker(fruit):
    return f"{fruit}+🍧"
def add_ice(juice):
    return f"{juice}+🧊"
def add_sugar(iced_juice):
    return f"{iced_juice}+🥂"
    
juice = juice_maker("사과")
juice2 = add_ice(juice)
comeplete_juice = add_sugar(juice2)

print(comeplete_juice)