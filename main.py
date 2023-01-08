days_of_week = ["Mon" ,"Tue", "Wed", "Thu" , "Fri"]

print(days_of_week.count("Mon"))
# list\\

name = "roh"

print(name.upper)
# .을 붙이면 뒤에 나오는 function은 함수들 method다
# method는 데이터에 결합된 function이다
# print(), random()<-와 같은 것들은 function// name. <- 에 들어가는 기능들은 method

numbers = ("1","2","3")

# tuples 는 불변성을 가진다. method를 추가하려고해도 추가할게 많이 없음

player = {
    'name' : 'imnofkcwifi',
    'age':12,
    'alive':True,
    'food':["noodle","pizza"]
}

print(player.get('age'))
print(player)
player.pop('age')
player['xp']=1500
print(player)
player['food'].append("ramen")
print(player)
# dicts 구조는 key*value 값 쌍으로 이루어져있다.