# ! -----> common function for list

# l1 = [6, 7, 8, 9,0,]
# print(len(l1))
# print(max(l1))
# print(min(l1))
# l1 =[6, 8, 9, "p", "u"]
# print(max(l1)) # --> error coz its a combination of and string
# print(min(l1)) #---> error coz its a combination of int and string

# l1 - [6, 7, 8,9,0, 8.89, 0.78]
# print(min(l1)) # -5

# l1 = [6,6,6, 7, 8, 9, 0,8.89, -5, 0.78]
# count() ---> how many num of times an element is repeated
# print(l1.count(6))

# ! some function which is specifically used for list

# to add element inside list
# ? insert(index_value,element) --> to add element at specific index position
# l1 =[6,6,6, 7, 8.89, -5, 0.78]
# pop() --> last element will be deleted
# l1.pop()
# print(l1)

# pop(index-value) ---> used to delete element at specific index
# l1.pop(4) # 4 is index value
# print(l1)

# remove (8.89)
# print(l1)

#* clear() ---> to complete delete all element in list
# l1.clear()
# print(l1)

# del -> to delete the list
# del l1 #or del(l1)
#print(l1)

# ? ----> join 2 lists

'''l1 = [9,0, 8]
l2 = ["p", "o", "t", 34]
print(l1+l2)'''

# ! or

'''# *extend() ----> to combie 2 lists
l1.extend(l2)
print(l1)'''


# ? ------> copy copy()
# l1= [6, 7, 8, 9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# ? ----> copy()
# l1=[6, 7, 8, 9, 3]
# l2=l1.copy()

# print(id(l1))
# print(id(l2))


# ! diff between shallow copy and deep copy
# * shall0w copy
# import copy
# l1 = [8, 9, 0,[3,2,1]]
# l2 = copy.copy(l1)
# l1 = copy.copy(l1)
#print(l1)
# print(l2)

'''# *deep copy
import copy
l1 = [8, 9, 0,[3,2,1]]
l2 = copy.copy(l1)
l1 = copy.copy(l1)
print(l1)
print(l2)'''

# * deep copy ----> to copt the list with nested with nested list

'''import copy
l1 = [8, 9, 0,[5,6], [3, 2,1]]
print(l1[-1][1]) --> to index nested list
l2 = copy.deepcopy(l1)
l1[-l].apped('cars')
print(l1)
print(l2)'''

# deep copy --> used to copy the list with nearext list

'''import copy
l1 = [3, 5, 6,7,[3,4,5],[2,3]]
print(l1[-1][1]) --> to index nested list
# (method)
l2 = copy.deepcopy(l1)
l1[-l].apped('cars')
print(l1)
print(l2)'''

'''# sort ---> arrange element in list in ascending or ascending or descending
l1 = [3, 5, 6,73,4,52,3]
l1.short()
print(l1[ '''#to arrange in ascending order


'''l1=[3,5,6,73,4,52,3]
l1. sort (reverse=true)
print(l1)'''# to arrange in descending order


'''l1=["w","r","u",9]
l1.short()
print(l1)'''# error different data type

# ///list constructor
# list() ---> to convert other collection datatypr to listb
# l3 =((8, 9, 0))
# print(list(l3))

# l4 = (8,9)
# print(list(l4))


# ! ----> nested list
# l1 =[8, 9,[0, 8,7],["p","o",'y',],[8, 't']
 # print(l1[-2][1] # --> 0
# print(l1[1:4])
# print(l1[1:-4])
     
# ? to delete "t" from l1
# l1[-1].remove('t')
# print(l1)

'''# ? combine these ["p", "o",'y.], [8, 't'] listts in l1 to ["p", "o",'y',8,'t']
l1=[-2].extend(l1(-1])
l1.pop(-1)
print(l1)'''

# ! -----> tuple
# *char of tuple

# 1.) tuple have to be surrounded by ()
# 2.) the elements inside tuple are not changable
# 3.) the elements inside tuple are indexed
# 4.) the element will execute in order
# 5.) it allow duplicate elements

# eg:
# t1 = (8, 8, 9, 6, 5,78,[9,0], (6,8),"hey", 9+6j)
# print(t1)
# print(type(t1))

# ? indexing, slicing are all same as list
'''l1 = (8)
print(type(l1)) # tuple

t1 = (8))
print(type)(l1)) '''# tuple

# t1 = 8,9
# print(type(t1)) # tuple

# t2 = 8,
# print(type(t2)) # tiple
# len(), min(), index(), count()---> all same list

# to add element inside tuple ---> cannot add
# cannot delete ant element from tuple
# * join 2 tuples
# t1 = (8, 9, 0)
# t2 =(6, 7, 8)
# print(t1+t2)

# to add all element inside list and tuple
# sum()
# l1 = (8, 9, 7, 6)
# print(sum(l1))
# * sort tuple
# t1 =(8, 9, 7, 6) 
# print(tuple(sorted(t1)))
# print(tuple(sorted(t1, reverse=true)))

# ? iterate list and tuples

# * iterate based on element
'''l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)'''


# * iterate based on index value
# l1 = [9, 8, 0, 6, 5, 8, 56]
# for i in range(0,len(l1)):
#    print(l1[i])

# ! ----> strings
# s1 = '0'
# print(type(s1))

# s1 ="u"
# print(type(s1))

# s1 = "hello world"
# * to access string
# print(s1)
# indexing and slicing ---> same as list and tuple
# print(s1[0:5])

# ----> common functions
# len(),min(), max(), index(), count()
# s1 = "hello world"
# print(len(s1))
# print(max)(s1))
# print(min(s1))

# ord() ---> used to find the ASCII value of character
# s1 = "hello world"

# ? to convert all characters to upper case
# print(s1.upper())

# ? to convert to lower case
# s1 = "HFREDGIOU"())

# ? strip()--> to eliminate the space in beginning and end of string
# s1 = " where are you?"
# print(s1.lstrip())
# print(s1.rstrip())
# print(s1.strip())


# split() ---> to split the world in srtring based on a character
# s1 = " where are you?"
# print(s1.split())
# print(s1.split("r" ))


# print(s1.split('e'))

# * replace() --> to replace a specific char in the string
# s1 = " where are you?"
# print(s1.replace('r','&&'))

# * title() --> to write the string in format of title
# s1 = 'never giveup'
# print(s12.capitalize())

# * capitalize() --> 1st char of string will be converted to capital
# s1 = "hello"
# s2 = 'world'
# print(s1+s2)

# s1 ='''
# how are you
# iam fine
# hey there'''

# * splines() --> used to split the string basedon lines
# print(s1.splitlines())

#* find() ---> to find the index based on a charachter
# s1 = "hello world"
# print(s1.find('z'))
# print(s1.index('z'))

#  *join() --->
# l1 = ["hey", "these"]
# print(" ".join(l1))
# print("&".join(l1))

# s1 = "welcome to all"
# * print(s1.endswith('1'))
# * print(s1.starswith('w'))

# s1 = "welcome to all"
# s1 = "67"
# print(type(s1))
# print(s1.isdigit())

# * print the string in reverse manner
# s1 = "welcome to all"
# print(s1[::-1])
# ! ---> Eg:1
# wap to find the number of case letters
# s1 = "hey these you are"
# count = 0
# for i in s1:
#    if i.islower():
#       count+=1
# print("the tatal of lower of case letter: ",count)

# ! ----> eg:2 r--->"$"
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt =bal.replaced(fst, "&")
print(fst+txt)



        




              

              
        

    

    




















