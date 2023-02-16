from math import *
#Day 5
#Level 1
#1
a = []
#2
b = [1, 2, 3, 4, 5, 6,7]
#3
len(b)
#4
b[0]

if len(b)%2 !=0:
    print(b[floor(float(len(b))/2)])

b[-1]    

#5
mixed_data_types = ['bilal' , 24, 1.85, 'single', 'Elazığ']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
len(it_companies)
#9
it_companies[0]
if len(it_companies)%2 !=0:
    print(it_companies[floor(float(len(it_companies))/2)])
it_companies[-1]
#10
it_companies[5] = 'Architect'
print(it_companies)
#11
it_companies.append('Aselsan')
print(it_companies)
#12
len(it_companies)
it_companies.insert(round(len(it_companies)/2), 'Tusaş')
print(it_companies)
#13
it_companies[2] = 'Havelsan'
print(it_companies)
#14
print(' # '.join(it_companies))
#15
print('IBM' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse = True)
print(it_companies)
#18
firstThreeCompanies = it_companies[0:3]
print(firstThreeCompanies)
#19
lastThreeCompanies = it_companies[-4:-1]
print(lastThreeCompanies)
#20
it_companies
len(it_companies)
middleItCompanies = it_companies[round(len(it_companies)/2)]
print(middleItCompanies)
#21
it_companies
it_companies.remove('Tusaş')
print(it_companies)
#22
print(len(it_companies))
it_companies.remove(it_companies[floor(len(it_companies)/2)])
it_companies.remove(it_companies[ceil(len(it_companies)/2)])
print(it_companies)
#23
print(it_companies)
it_companies.remove(it_companies[-1])
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#27
full_stack = front_end + back_end
print(full_stack)
full_stack.index('Redux')
full_stack.insert(full_stack.index('Redux')+1,'Phyton')
full_stack.insert(full_stack.index('Redux')+2, 'SQL')
print(full_stack)
#Level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages[(len(ages)//2)-1]
print(ages)
ages[0]
ages[-1]
ages.append(ages[0])
ages.append(ages[-1])
print(ages)
#median age
ages.sort()
if len(ages)%2 == 0 :
    print('Median of ages : ', ((ages[len(ages)//2 - 1]) + ages[len(ages)//2])/2)
else :
    print('Median of ages : ' , ages[(len(ages)//2)])    

#average
avr = sum(ages) / len(ages)
print(avr)

#range of the ages
ages.sort(reverse = True)
print(ages)
rangeOfTheAges = ages[0] - ages[-1]
print(rangeOfTheAges)

#Compare
print(ages[-1] > avr)
print(ages[-1] < avr)

print(ages[0] > avr)

#1
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
  'Zimbabwe']

if len(countries)%2 == 0 :
    print('Middle Countries : ', countries[len(countries)//2 - 1] , 'and' , countries[len(countries)//2])
else :
    print('Middle Countrie : ' , countries[(len(countries)//2)])    

#2
firstPart , secondPart = countries[0:len(countries)//2] , countries[len(countries)//2:]

print(firstPart)
print(secondPart)

#3
someCountries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

firstThree , rest = someCountries[0:3], someCountries[3:]

print(firstThree)
print(rest)
















































































