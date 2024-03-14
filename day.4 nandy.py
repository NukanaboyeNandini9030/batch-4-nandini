# ex:1
'''i=20
while i>31:
    if i ==27:
     break
    print(i)
    i+=1'''
# method :2
'''i = 20
while i<31:
    print(i)

    if i==27:
        break
    i+=1'''
 # method :3   
'''i = 20
while i<31:
    print(i)

    if i==27:
        break
     i+=1'''
# continue
'''i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=+1'''
# method
'''i=20
while i<31:
    i=+1
    if i==27
        continue
    print(i)'''
 # method
 
''' =12
temp=0
while i<23:
    temp=temp+i
    i+=1
print(temp)'''
# method
'''i=20
sum=0
while i<26:
    sum=sum+i
    i+=1
temp=(sum/5)
print(temp)'''
# ! -----> Nested for loop
# Eg:1
'''for row in range(1, 3+1):
    for col in range(1,4+1):
        print(row,col)'''

'''for row in range(4):
    for col in range(4):
        print(row,col)'''
        
  
'''for row in range(4):
    for col in range(4):
        print("*")'''

'''for i in range(4):
    for j in range(4):
        print("*",end="")
    print()'''

'''end = 0
for row in range(5):
    for col in range(5):
        end= end+1
        print(row, end="")
    print()'''


# ! to point stars in right angled triangle

'''for row in range(0, 6):
    for col in range(0,row+1):
        print("*", end="")
        print()'''
    
'''for row in range(0, 6,-1):
    for col in range(0, row,):
        print("*", end="")
        print()'''

'''for row in range(0, 6,-1):
    for col in range(0, row,):
        print("*", end="")
        print()'''
'''for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or  row ==0 or row ==5-1:
            print("*", end="")
        else:
            print(" ", end=" ")
print()'''

'''for row  in range(0, 5):
    for col in range(0, 6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or(row==2 and(col>1 and col<=5)))):
            print("*", end="")
        else:
            print(" ", end=" ")
    print()'''
# ---> datatypes

'''primary
number---> int, float complex
string
boolean
none

# 
collection
list
tuple
set
dictionary'''

# ? ---> list


# 1.)if the collection of elements are sorouned by square brackets, it is considered
# to be list
 # ! eg:
 #11 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]'''

 
#1.)list have to be sorrouned in the  list are changable)
 #.2) it is mutable (the element in  the are changable)
 #.3) every elements inside list will be ordered format
 #.4) the elements inside list will be ordered format
 #.5) it can hold duplicate values
 #.6) its heterogenous


 # ton accer the element in list
 # L1 = [1, 4, 1. 7,89.7, 7.5, "p", "i"]
 # print(11)


# ----> indexing
# the collection datatypes like list, string, the element will be alloted
# with pre-defined  unique value called index value

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# negative indexing --> srarts with -1 from right hand side


# ? --> positive indexing
# lst1 = [1, 4, 1, 7, 7.5,"p","i"]
# print (lst1[0])
# print(lst1[4])
# print([lst[20])-->error

# ? -----> Negative indexing
# lst1 = [1, 4, 1, 7, 89.7.5,"p","i"]


# print(lst1[-1])
# print(lst1[-5])

# ?---> slicing
#lst1 =[1, 4, 1, 7,89.7,7.5, "p", "i"]
#lst1[star_index:end_index:step]

# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:])


# print(lst1[0:7:1] # lst1[0:7] --> both are saame
# print(lst1[0:7:2[)

# trail = int(input())

'''lst1 =[1,4, 1, 7,89.7,"p","i"]
print(lst1[-4:1])
print(lst1[-1:-4])
print(lst1[-7:-1])
print(lst1[-7:-1:2])'''

#! to insert ot add element inside list


# append() --> used to add element at last position of list
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)
      



















 
 

        

      
      
        
      
    
    
    














    
    
    
    

 
    
    
    














    
    
    
    
