#Day 13
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for row in list_of_lists for number in row]
print(flatten_list)

#3
lst = [(i , 1 , i , i**2, i**3 , i**4 , i**5) for i in range(0,11) ]
print(lst)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flatten_countries = [[i[0].upper() if j==0 else i[0][:3].upper() if j==1 else i[1].upper() for i in country for j in range(3)] for country in countries] 

print(flatten_countries)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

out = [{'country': tup[0].upper(), 'city': tup[1].upper()} for lst in countries for tup in lst]
print(out)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

full_names = [name[0] + ' ' + name[1] for lst in names for name in lst ]
print(full_names)

#7

slope = lambda x1,x2,y1,y2 : (y2-y1)/(x2-x1)
slope(5,3,4,6)


















