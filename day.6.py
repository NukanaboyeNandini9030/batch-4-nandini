# s1 =input("enter the string")
# s1=s1[0:1].upper()+s1[1:len(s1)-1] +s1[len(s1)]
# print(s1)


# s1 = " hello world"
# fst = s1[0].upper()
# lst = s1[-1].upper()
# print(fst+s1[1:len(s1)-1]+lst)
'''n = 128
temp = n
while n!=0:
    temp = n%10
    check= temp % temp
    if check!=0:
          f1 = 1
    n =n//10'''

    

'''l1=[9,8,0,7]
l2=[7,6,5,4]
l3=[]
for val in range(len(l1)):
    ans =l1[val]+l2[val]
    l3.append(ans)
print(l3)'''
# ! -----> set
 
# ? charctristics of set
# 1.)# set can be created using {}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unordered
# 5.) hterogeonous
# 6.) mutable or changable

# Eg:1
# s1 = {9, 9, 89, 7.76, 8+7j, (8,7,5), "truck", 'e'}
# #print(s1)

# * Eg:2
# #s2 = {5, 8, 98,[9,0]}
# print(s2) --> error

# Eg:3
# min(), max(), len()
# * eg
# ? to add element inside set

# s1 = {8, 78, 67, 'u'}
# add()
# s1.add(43)
# print(s1)


# update()
# s1.update([9, 0])
# print(s1)

# ? to delete element inside set
# s1 = {8, 78,67, 'u'}

# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove()
# s1. remove(978)
# print(s1)

# discard()
# s1.discard(8967)
# print(s1)
# clear()
# l1 ={}
# print(type(l1)) --> datatypes is dict

# s1 = set() # to create empty set
# print(type(s1))

# s1 = {8, 9, 0}
# s1.clear()
# print(s1)

# del s1
# print(s1)


# *join the sets
# s1 = {9,0,8}
# s2 = {9.90, "card", 't', 56}
# union() --> ombine 2 sets
# s3 = s1.union(s2)
# print(s3)

# intersection() --> to get common elements inside set
# s1 = {4, 5, 6,}
# s2 = {5, 6, 7, 8}
# print(s1.intersection(s2))

# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))


# isdisjoit(), issubset(), issuperset()
# s1 = {8,9,0}
# s2 = {6, 7, 5, 8, 9, 0}

# print(s1.issubset(s2))
# print(s2.issuperset(s1))

# s1 = {1,2,3,4}
# s2 = {7,6,9,5}
# for val in s1:
#   if val in s2:
#        str1 = "Its joint set"
# print(str1)

# ! ----> dictionary
# eg:1
# d1 = {1:100, 'a':200,  4.5:"hello"}
# print(d1)
# print(len(d1))
# ? char of dictionary
# 1.) have to be surrounded by {}
# 2.) it have to be in the form of key, value pair
# 3.) it is unindexed
# 4.) duplicate keys are not allowed, duplicate values are allowed
# 5.) it is unindexed
# 6.) key does not allowed mutable datatypes, values allowed mutable datatype


# d1 = {1:100, 2:200, 3:300, 4,400}
# * to access the values

# print(d1)
# or
# to access the value, have to use key
# print(d1[1]) # o/p --> 100

# ? some common function

# len(),min,max()
# print(min(d1))
# print(macx(d1))
# ? to find min, max based on values
# print(min(d1.values()))
# print(max(d1.values()))

# ? dictionary based functions
# to add element(key and value pair)in dict
# d1 = {1:100, 2:200, 3:300 4:400}
# d1[5] = 500
# print(d1)

# ? to replace a value in dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[5] = 500
# print(d1)

# ? element from dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# popitem() # ----> to delete last key value pair in dict
# d1.popitem
# print(d1)

# pop()
# d1. pop(2) # 2 is the key in dictionary
# print(d1)

# clear(), del
# * join 2 dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {"a":"apple", "b":"boy", "g":"game"}
# d1.update(d2)
# print(d1)

# get ----->
# d1={ {1:100, 2:200, 3:300, 4:400}
# print(d1[90])
# print(d1)

# to print all the keys
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())

# iterating dictionary
# for val in d1: # to iterate keys alone
# print(val)

# for val in d1.values(): # to iterate values alone
#nprint(val)
# to get both key and values
# for key, val in d1.items():
# print(key, val)



'''# ! problem:1
n = int(input("enter num of times : "))
integer=[]
float_float
string=[]
for val in range(n):
        value = eval(input("enter the values: "))
        if type(value)==int:
             integer.append(value)
        elif type(value) ==  float:
            float_value.append(value)
        elif type(value) == str:
            string.append(value)
else:
        print("pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)'''

'''set1 = {10, 20, 30, 40, 50}
set2 = {30,40, 50, 60,70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)'''




        

l1 = [1,2,3,4] 
l2 = ["a","b","c", "d"]
d1 = {}
for val in range(len(l1)):
   d1[l1[val]] =l2[val]
print(d1)





 











      \




      
