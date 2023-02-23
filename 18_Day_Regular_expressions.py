import re
#Day 18
##Level 1
#1
paragraph = '''I love teaching. 
If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the 
capabilities to develop an application what else can you love.'''

def get_wordcount(sentence):
    repattern = r'[A-Za-z]*[^\W]' 
    wordset = set(re.findall(repattern, sentence, re.I)) 

    word_count_list = [] #

    for i in wordset:
        word_tup = (len(re.findall(i + '\W', sentence)), i) 
        word_count_list.append(word_tup) 

    return sorted(word_count_list, reverse=True) 


print(*get_wordcount(paragraph), sep='\n')

#2 
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) 

def extract_numbers(text):  
    repattern = r'-?\d+'
    return [int(i) for i in re.findall(repattern, text)] 


points = sorted(extract_numbers(paragraph))

distance = points[-1] - points[0]

print(f'{points[-1]} - {points[0]} = {distance}')


##Level 2
#1
def is_valid_variable(text): 
    repattern = r'^[A-Za-z|_][A-Za-z0-9_]*$' 
    if re.match(repattern,text) != None:
        
        return True
    else:
      
        return False










