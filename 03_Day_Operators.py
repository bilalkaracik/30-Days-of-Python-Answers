from math import *
#Dat 3
#1
age = 24
#2
height = 1.85
#3
c = 1 + 2j
#4
base = int(input('Please enter base : '))
height = int(input('Please enter height : '))
area = int(0.5 * base * height)
print('Area of the Triangle :', area)
#5
a = int(input('Please enter side a :'))
b = int(input('Please enter side b :'))
c = int(input('Please enter side c :'))
perimeter = a + b  + c
print('Perimeter of the triangle : ', perimeter)
#6
length = int(input('Please enter length : '))
width = int(input('Please enter width : '))
perimeter_rectangle = 2 * (length + width)
area_rectangle = length * width
print('Length : ' , perimeter_rectangle)
print('Area : ', area_rectangle)
#7
r = int(input('Please enter radius : '))
area_circle = pi * r * r
circumference = 2 * pi * r
print('Area of Circle : ', area_circle)
print('Circumreference : ', circumference)
#8
y = 2x - 2 
##Burayı yapamadım değer koyma yöntemini bulamadım.
##Berkaya sor.
#9
o = [2,2]
t = [6,10]

m = (t[1] - o[1]) / (t[0] - o[0])
print('Slope : ', m)

euclidian_dictance = ((t[1] - o[1]) ** 2 + (t[0] - o[0]) ** 2) ** 0.5
print('Euclidian Distance : ' , euclidian_dictance)

#10
##8'i yapamadığım için karşılaştırma yapamıyorum.

#11
a = x
y = x**2 + 6*x + 9

a = 5
y
a = 3
y
delta = 6**2 - 4*2*9
x1 = (-6 + delta ** 0.5)/2*2
x2 = (-6 - delta ** 0.5)/2*2
x1
x2
a = -3
y
###11.soruda bir gariplik var.

#12
len('python')
len('dragon')
len('python') == len('dragon')
len('python') != len('dragon')

#13
print('on' in 'python' and 'on' in 'dragon')

#14
print('jargon' in 'I hope this course is not full of jargon.')

#15
print('on' not in 'dragon' and 'python')

#16
len('python')
float(len('python'))
str(len('python'))

#17
def number(x):
    if x%2 == 0:
        print('even')
    else:
        print('odd')
number(5)     

#18
7 // 3 == int(2.7)   

#19
type('10') == type(10)

#20
int('9.8') ==10

#21
hours = int(input('Please enter your hours : '))
rate = int(input('Please enter your rate : '))
weekly_earning = hours * rate
print('Your weekly earning is ' , weekly_earning)

#22
year = int(input('Please enter number of years : '))
lived = year * 365 * 24 * 60 * 60 
print('You have lived for ', lived , 'seconds.')

#23
print(""" 1 1 1 1 1
 2 1 2 4 8
 3 1 3 9 27
 4 1 4 16 64
 5 1 5 25 125 """)






















































