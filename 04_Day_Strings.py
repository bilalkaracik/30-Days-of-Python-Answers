#Day 4
#1
print('Thirty ' + 'Days ' + 'Of ' + 'Python ')
#2
print('Coding ' + 'For ' + 'All')
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
company.upper()
#7
company.lower()
#8
company.capitalize()
company.swapcase()
company.title()
#9
company.strip('Coding')
#10
'Coding' in 'Coding For All'
#11
company.replace('Coding', 'Python')
#12
'Python for Everyone'.replace('Everyone', 'all')
#13
company.split()
#14
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
#15
company[0]
#16
company[-1]
#17
company[10]
#18
PFE = 'Python For Everyone'
#19
CFA= 'Coding For All'
#20
CFA.index('C')
#21
CFA.index('F')
#22
CFA.rfind('I')
#23
'You cannot end a sentence with because because because is a conjunction'.find('because')
#24
'You cannot end a sentence with because because because is a conjunction'.rindex('because')
#25
a = 'You cannot end a sentence with because because because is a conjunction'
print(a[0:30] + a[57::])
#26
a.find('because')
#27
#25 ile aynı.
#28
'Coding For All'.startswith('Coding')
#29
'Coding For All'.endswith('coding')
#30
'   Coding For All      '.strip(' ')
#31
'30DaysOfPython'.isidentifier()
'thirty_days_of_python'.isidentifier()
#32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(libraries)
print(result)
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
#35
radius = 10
area = 3.14 * radius **2
print('The area of a circle with %d is %d meters square.'%(radius,area))
print('The area of a circle with {} is {} meters square.'.format(radius,area))
print(f'The area of a circle with {radius} is {area} meters square.')
#36
a = 8
b = 6
print('{} + {} = {}'.format(a, b , a+b))
print('{} - {} = {}'.format(a, b , a-b))
print('{} * {} = {}'.format(a, b , a*b))
print('{} / {} = {}'.format(a, b , a/b))
print('{} % {} = {}'.format(a, b , a%b))
print('{} // {} = {}'.format(a, b , a//b))
print('{} ** {} = {}'.format(a, b , a**b))


print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')



















































