#Day 14
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##Level 1
#1
#The map() function is a built-in function that takes a function and iterable as parameters.
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
#It filters the items that satisfy the filtering criteria.
#The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. 
#However, it does not return another iterable, instead it returns a single value.

#2
#Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.
#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

#3
numbers = [0,1,2,3,4,5,6]

def square(x):
    return x**2

numbers_squared = map(square, numbers)
print(list(numbers_squared))

def even(x):
    if x %2 == 0 :
        return True
    return False

filtered_even = filter(even, numbers)
print(list(filtered_even))

from functools import *

numbers_str =['1', '2', '3', '4']

def add_two_nums(x,y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)

print(total)

#4
for i in countries :
    print(i)

#5
for i in names:
    print(i)

#6
for i in numbers:
    print(i)

##Level 2
#1

def upper_countries(x):
    return x.upper()

new_upper_countries = map(upper_countries, countries)
print(list(new_upper_countries))


#2
def square(x):
    return x**2

squared = map(square, numbers)
print(list(squared))

#3
def upper_names(x):
    return x.upper()

names = map(upper_names, names)
print(list(names))

#4
def filter_countries(x):
    if 'land' in x:
        return True
    return False

filtered = filter(filter_countries, countries)
print(list(filtered))

#5
def char(x):
    if len(x) == 6:
        return True
    return False

chared = filter(char, countries)

print(list(chared))

#6
def char(x):
    if len(x) >= 6:
        return True
    return False

char_more = filter(char, countries)
print(list(char_more))

#7
def char(x):
    if x[0] == 'E':
        return True
    return False

E = filter(char , countries)
print(list(E))

#8
summation_of_square = reduce(lambda x,y: x+y, map(square,numbers))

print(summation_of_square)

#9
lst = ['a' , 1 , 2  , 'b', 'c']
def get_string_list(x):
    if type(x) == str:
        return True
    return False

filter_lst = filter(get_string_list, lst)

print(list(filter_lst))

#10
from functools import *
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_all(x,y):
    return int(x) + int(y)
    
sums = reduce(sum_all, numbers)
print(sums)

#11
def concanate_countries(x,y):
   return str(x) + ',' + ' ' + str(y)     

su = reduce(concanate_countries, countries)

print(su)

#12
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries(x):
    if 'land' in x:
        return True
    return False
countriess = filter(categorize_countries, countries)

print(list(countriess))

#13
new = []
def get_first_ten_countries(x):
    return x

news = map(get_first_ten_countries, countries[0:10])

for country in news:
    new.append(country)

print(new)

#14
new1 = []
def get_last_ten_countries(x):
    return x

news1 = map(get_last_ten_countries, countries[-10:-1])

for country in news1:
    new1.append(country)

print(new1)













































