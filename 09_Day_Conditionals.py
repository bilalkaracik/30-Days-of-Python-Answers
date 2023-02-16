#Day 9
##Level 1
#1
age = int(input('Enter your age : '))
if age >= 18:
    print('You are enough to drive.')
else :
    print('You need' ,18-age, 'more years to learn to drive.')
    
#2
my_age = 24
your_age = int(input('Enter your age : '))
if my_age > your_age and my_age - your_age > 1 :
    print('I am older than you')
elif your_age > my_age and your_age - my_age > 1 :
    print('Your are older than me.')
else:
    if my_age > your_age and my_age - your_age <= 1 :
        print('We are almost the same age.')
        
    elif your_age > my_age or your_age - my_age <= 1 :
        print('We are almost the same age.')
        
#3
a = int(input('Please enter first number : '))       
b = int(input('Please enter second number : ')) 
if a > b :
    print(f'{a} greater than {b}')
elif a < b:
    print( f'{a} is smaller than {b}')
else :
    print(f'{a} equal to {b}')

##Level 2
#1
note = int(input('Please enter the note : '))
if 100 > note >= 90 :
    print('Note : A' )
elif 90 > note >= 70 :
    print('Note : B' )
elif 70 > note >= 60 :
    print('Note : C' )    
elif 60 > note >= 50 :
    print('Note : D' )
else :
    print('Note : F' )  
    
#2
month = input('Please enter month : ')
if month == 'September' or 'October' or 'November' :
    print('Season is Autumn.')
elif month == 'December' or 'January' or 'February' :
    print('Season is Winter.')   
elif month == 'March' or 'April' or 'May' :
    print('Season is Spring.')
elif month == 'June' or 'July' or 'August' :
    print('Season is Summer.')            

#3
fruit = input('Please enter fruit : ')
fruits = ['banana', 'orange', 'mango', 'lemon']        

if fruit not in fruits :
    fruits.append(fruit)
    print(fruits)
else :
    print('That fruit already exist in the list.')
    
##Level 3
#4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#i
from math import *
print('skills' in person)
a = len(person['skills'])
if a%2 == 0 :
    a1 = a/2 - 1 
    a2 = a/2
    print('First : ', person['skills'][a1] , 'Second : ', person['skills'][a2])
elif a%2 != 0 :
    b1 = ceil(float(a / 2))
    print(person['skills'][b1])    

#ii
print('skills' in person)
if 'Python' in person['skills']:
    print(person['skills'])
else :
    print('Python not in skills.')

#iii
if person['skills'] == 'JavaScript' and 'React' :
    print('He is a front end developer.')
elif person['skills'] == 'Node' and 'Python' and 'MongoDB' :
    print('He is a backend developer.')    
elif person['skills'] == 'Node' and 'React' and 'MongoDB' :
    print('He is a fullstack developer.')
else :
    print('\'unknown title\' - for more accurate results more conditions can be nested!')

#iiii
if person['is_marred'] == True and person['country'] == 'Finland' :
    print('Asabeneh Yetayeh lives in Finland. He is married.')
    




























    
    
    




















    
    
    
    
    
    
    
    
    
    
    
    











































          
    
    
