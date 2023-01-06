from random import randint, random
# 코드가 느려질수있으므로 import 해서 module에서 function을 가져온다
# https://docs.python.org/ko/3/library/index.html



if 5<19:
    print("hi")
    
a = 10
# 10이라는 값을 a라는 variable에 넣는다는 뜻

if a == 10:
    print('true')
# 왼쪽 a이 오른쪽 10과 같은지 확인

password_correct = True

if password_correct:
    print("take this money")
else:
    print("wrong password")

winner = 10

if winner >10:
    print("winner is grater than 10")
elif winner <10:
    print("winner is less than 10")
elif winner!=10:
    print("noooo")
else:
    print("winner is 10")

age = input("how old are you?")

print("user answer", age)

print(type(age))

age2 = int(input("how old are you?"))

if(age2>20):
  print("go ahead",age2)
elif(age2>100):
    print("wait waht")
else:
    print("nah")
    
distance = 0
while distance <= 20 :
    print("gogogogogo", distance)
    distance = distance +1

# casino game

pc_choice = randint(1,50)
user_choice = int(input("choose a number"))
playing = True

while playing:

    if user_choice==pc_choice:
        print("you won!",pc_choice)
        playing =False
    elif user_choice>pc_choice:
        print("high", pc_choice)
    elif user_choice<pc_choice:
        print("low",pc_choice)


