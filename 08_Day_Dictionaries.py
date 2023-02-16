#Day 8
#1
dog = {}
#2
dog['name'] = 'Johny'
dog['color'] = 'black'
dog['breed'] = 'pitbull'
dog['legs'] = 4
dog['age'] = 3
print(dog)
#3
student = {
    'first_name' : 'bilal',
    'last_name' : 'karacık',
    'gender' : 'male',
    'age' : 24,
    'marital status' : 'single',
    'skills' : ['Python' , 'SQL' , 'Matlab'],
    'country' : 'Türkiye',
    'city' : 'Ankara',
    'address' : 'Cankaya'}
#4
print(len(student))
#5
print(len(student['skills']))
print(type(student['skills']))
#6
student['skills'].append('C++')
print(student['skills'])
#7
student.keys()
#8
student.values()
#9
studentList = student.items()
print(type(studentList))
#10
del(student['address'])
print(student)
#11
del student

















