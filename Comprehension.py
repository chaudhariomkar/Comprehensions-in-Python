""""""
"""
Comprehension - Comprehensions in python are a concise way to create sequences.
[expression/operation on i for i in iterable (it can return its element one at a time - we can use loop)]

List Comprehension
We will get a new list by some operation over the sequence but to do this we need a compact code
Shorter Syntax is the main key in list comprehension (Single line solution)
Syntax : [expression/operation for loop] *Output in list format
"""
nm = ['ajay','deepali','kiran','kanchan','yogesh','salman','ajit'] #give a converted list of all names in upper case
#pythonic way
conv = []
for n in nm:
    conv.append(n.upper())
print(conv)
#by list comprehension
print([n.upper() for n in nm]) #Uppercase
print([n.title() for n in nm]) #Title

#Can we perform more than one operation in list comprehension(2 conversion : 1-upper and 2-title)
print([(n.upper(),n.title()) for n in nm])
#Expected output--> [['ram',3],['sham',4]]
print([[n,len(n)] for n in nm])

#Fetch a list of employees whose name starts with a
print([n.startswith('a') for n in nm]) #output in boolean format
print('New Approach') #Another approach
print([i for i in nm if i.startswith('a')]) #actual output

#List of 1-10 numbers
print([i for i in range(1,11)])
#List of square of 1-10 numbers
print([i**2 for i in range(1,11)])
#List of tuple for 1-10 numbers [(num,num*num)]
print([(i,i*i) for i in range(1,11)])

#Condition based comprehension
#[expression/operation for i in sequence if condition]
#List of only even numbers
print([i for i in range(1,11) if i%2 == 0])
#List of only odd numbers
print([i for i in range(1,11) if i%2 != 0])

#If we want to check 2 condition then
#[expression1 if condition else expression2 for i in sequence]
gender = ['Male','Female','Female','Male','Male','Female'] #convert Male as 1 and Female as 0
print([1 if g == 'Male' else 0 for g in gender])
gender1 = ['Male','Other','Female','Female','Other','Male','Male','Female','Other'] #convert Male as 1
print([1 if g == 'Male' or g == 'Other' else 0 for g in gender1])

#----------------------------------------------------------------------------------------

#Dict Comprehension
#Syntax {key:value for i in sequence}
name = ['amit','sarita','namit','subhash'] #{'amit':len(amit)}
print({i:len(i) for i in name})
#dict {1:1,2:4,3:9......10:100} dict of num and its square
print({i:i**2 for i in range(1,11)})
#dict of only odd numbers {1:1,2:4,3:9......10:100} dict of num and its square
print({i:i**2 for i in range(1,11) if i%2 != 0})
#dict of odd numbers and its square & dict of even num and its cube
print({i:i*i if i%2 != 0 else i**3 for i in range(1, 11)})

n = 'rajendra' #fetch lists of Vowels
vowels = ['a','e','i','o','u']
print([i for i in n if i in vowels])
#Find index of vowels
print([n.find(i) for i in n]) #find index
print(n.find('a')) #find index
#to get an index of each char/element - use enumerate
#enumerate gives 2 things - returns a tuple (index,value/element)
for i in enumerate(n):
    #print(i)
    if i[1] in vowels:
        print(i[1],'index',i[0])
