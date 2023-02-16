#Day 12
from random import randint
import string
##Level 1
#1
def random_user_id():
    random = ''
    alphaNum = string.ascii_letters + string.digits
    
    for i in range(0,7,1):
        rand_index = randint(0,len(alphaNum)-1)
        random += alphaNum[rand_index]
    return random        

random_user_id()

#2
def user_id_gen_by_user():
    user_count = int(input('Number of Users: '))
    id_size = int(input('Length of userid: '))
    alpha_num = string.ascii_letters + string.digits # Alphanumeric string for generation
    user_ids = [] # Empty list of user ids to be populated
    
    for user in range(0,user_count,1): 
        new_id = ''
        for i in range(0, id_size, 1):
            rand_index = randint(0, len(alpha_num)-1)
            new_id += alpha_num[rand_index]
        user_ids.append(new_id)
    
    return user_ids

#3
def rgb_color_gen():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    return red , green , blue

rgb_color_gen()

##Level 2
#1
def list_of_hex_colors(num_to_gen):
    hex_colors = []

    for hex_color in range(0,num_to_gen,1):
        new_color = ''
        for i in range(0, 6, 1):
            new_color += string.hexdigits[randint(0, 16)]
        
        hex_colors.append('#'+new_color)

    return hex_colors

print(list_of_hex_colors(6))

#2
def list_of_rgb_colors(num_to_gen):
    rgb_colors = []

    for rgb_color in range(0, num_to_gen,1):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        rgb = red, green, blue

        rgb_colors.append('rgb' + str(rgb))
    return rgb_colors

print(list_of_rgb_colors(3))

#3
def generate_colors(ctype, num_to_gen):
    if ctype == 'hexa':
        return list_of_hex_colors(num_to_gen)
    elif ctype == 'rgb':
        return list_of_rgb_colors(num_to_gen)
    else:
        print('Invalid Color Type [hexa, rgb]')

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']

##Level 3
#1
def shuffle_list(lst):
    shuffled_lst = []
    for i in range(0, len(lst)):
        shuffled_lst.insert(randint(0, len(lst)), lst[i])
    
    return shuffled_lst
   
list_to_shuffle = ['sam', 'ty', 'gaming', 'age', 'lame', 'somethingmore']
print(shuffle_list(list_to_shuffle))

#2
def array_of_seven():
    numbers = set({})
    while(len(numbers) < 8):
        numbers.add(randint(0, 9))
    return numbers

print(array_of_seven())












































