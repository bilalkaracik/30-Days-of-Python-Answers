#Day 6
##Level 1
#1
tpl = ()
#2
tpl = ('mustafa', 'zeynep')
#3
tpl1 = ('bilal',)
tpl = tpl + tpl1
print(tpl)
#4
len(tpl)-1
#5
parents = ('nezahat' , 'mehmet')
family_members = parents + tpl
print(family_members)

##Level 2
#1
parent , siblings =  family_members[0:2] , family_members[2:]
print(parent)
print(siblings)
#2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal = ('cow' , 'snake')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#4
len(food_stuff_lt)
part1 , part2 = food_stuff_lt[0:6] , food_stuff_lt[6:]
print(part1)
print(part2)
#5
part3 = food_stuff_lt[0:3] + food_stuff_lt[-3:]
print(part3)
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)














