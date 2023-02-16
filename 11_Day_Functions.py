from math import *
#Day 11
##Level 1
#1
def add_two(num1 , num2):
    sum = num1 + num2
    return sum

add_two(5,8)

#2
def are_of_circle(r):
    area = pi * (r**2)
    return area

are_of_circle(10)

#3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if num == int and float:
            for num in nums:
                total += num
            return total
        else :
            print('none')
            break
                
          
add_all_nums(1,2,3, 'a')

#4
def convert_celsius_to_fahrenheit(C):
    F = (C * 9/5) + 32
    return F

convert_celsius_to_fahrenheit(120)

#5
def check_season(month):
    if month == 'September' or 'October' or 'November' :
        print('Season is Autumn.')
    elif month == 'December' or 'January' or 'February' :
        print('Season is Winter.')   
    elif month == 'March' or 'April' or 'May' :
        print('Season is Spring.')
    elif month == 'June' or 'July' or 'August' :
        print('Season is Summer.') 

#6
def calculate_slope(x1 , x2 , y1 , y2):
    slope = (y2 - y1) / (x2 - x1)
    print('Slope : ', slope)

calculate_slope(3,5,9,10)

#7

def solve_quadratic_eqn (a,b,c) :
    print('Function : ' , f'{a}*(x**2) + {b}*x + {c} = 0')
    delta = b**2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / 2 * a
    x2 = (-b - delta ** 0.5) / 2 * a
    print('First answer : ' , x1,
          'Second answer : ' , x2)

solve_quadratic_eqn(1, 6, 9)

#8
def print_list(lst):
    for i in lst:
        print(i, end = ' ')

print_list([1,2,3,4,5])

#9
reverse = []
def reverse_list(array):
   for i in array:
       reverse.insert(0,i)
   return(reverse)        

print(reverse_list([1, 2, 3, 4, 5]))

print(reverse_list(["A", "B", "C"]))

reverse = []
def reverse_list1(array):
   for i in range(len(array)-1,-1,-1):
       reverse.append(array[i])
   return(reverse)  

print(reverse_list1(["A", "B", "C"]))
reverse_list=[1, 2, 3, 4, 5]
rev_array = reverse_list[::-1]
rev_array
#10
new_lst = []
def capitalize_list_items(lst):
    for i in lst:
        new_lst.append(i.capitalize())
    print( new_lst)

capitalize_list_items(['ali', 'veli'])

#11
def add_item(lst, item):
    app_list = lst
    app_list.append(item)
    return app_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))  

#12

def remove_item(lst, item):
    remove_list = lst
    remove_list.remove(item)
    return remove_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))

#13
def sum_of_numbers(x):
    sum = 0
    for i in range(x+1):
        sum = sum + i
    return sum     

sum_of_numbers(10)    

#14
def sum_of_odds(y):
    sum = 0
    for i in range(y+1):
        if i%2 == 0:
            sum = sum + i
    return sum                    
            
sum_of_odds(10)

#15
def sum_of_even(y):
    sum = 0
    for i in range(y+1):
        if i%2 != 0:
            sum = sum + i
    return sum  
sum_of_even(5)

##Level 2
#1
even_n = []
odd_n =[]
def evens_and_odds(n):
    if n > 0:
        for i in range(n+1):
            if i%2 == 0:
                even_n.append(i)
            else :
                odd_n.append(i)
    print('The number of evens are : ' , len(even_n))
    print('The number of odds are : ' , len(odd_n))                      
 
evens_and_odds(150)                

#2

 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
































        






























































































