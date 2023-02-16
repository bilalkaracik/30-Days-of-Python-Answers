#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
##Level 1
#1
len(it_companies)
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Havelsan' , 'Aselsan'])
print(it_companies)
#4
it_companies.remove('Oracle')
print(it_companies)
#5
#If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
##Level 2
#1
A.union(B)
#2
A.intersection(B)
#3
A.issubset(B)
#4
A.isdisjoint(B)
#5
A.union(B)
B.union(A)
#6
A.symmetric_difference(B)
#7
del A, B
del fruits , it_companies

###Level 3
#1
agesSet = set(age)
if len(agesSet) > len(age):
    print('Length set bigger than length list.')
elif len(agesSet) < len(age):
    print('Length list bigger than length set.')
else:
    print('Length set equal the length list.')
    
#2
#String : Characaters.
#list : Ordered and changeable.
#Tuple : Ordered and immutable.
#Set : Un-ordered and un_indexed

#3
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence.split(' ')
print('Unique words : ', len(set(sentence.split(' '))))


























