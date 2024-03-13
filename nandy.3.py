# name, age,
# name = int(input("enter the name:")
# age = int(input("Enter the nation:")

# if age>=18 and nationality=="Indian":
#  print("eligible for vote")
# else:
#   print"not eligible")

# Eg:3
# ? take values of length and breadth of a
# ? from user and check if if is square or not.


# length = int(input())
# breath = int(input())
# if length==breath
#    print("its a aquare")
# else:
#    prinf("its not aquare")

# !   Eg:4
# python program to check whether the
# give integer is a multiple of both 5 and 7

# n = int(input("enter the number:"))
# if n%5==0 and n%7==0:
#    print("yes")
 #    print("no")
# else
 # ! Eg:5
 # write a program to accept the cost price of a bike and diplay the
 # road tax to be paid
 #  accoding to the following criteria :

#    cost price (in Rs)              Tax
#    > 100000                         15 % + discount 6%
#    > 50000 and <= 100000             10%
#    < 50000                            5%
# price =int(input("enter the price: "))
# amount = 0
# if price >=100000:
#    discount = 100000*(15/100)
#   value = price-discount
#    tax=value*(15/100)
#   total=value+tax
# else:
#    tax = price*(5/100)
#    total = price+tax
 #   print("the onroad cost of bike is: ",total)
 # Eg:6
# a = 7
# b = 9
# c = 30

# if a> and a>c:
#   print("b is greater")
#elif b>a and b>c:
#    print("b is greater")
# elif c>a and c>b:
#    print("c ois greater")

# A school has follwing rules for grading system:
# a. below 25 -F
# b. 25 to 45   -E
# c.45 to  50   -D
# d. 50 to  60  -C
# e. 60 to  80 B
# f. above 80 - A
# mark =int(input("enter mark:"))
          
# if mark>=80 and mark<=100:
#         print("A")
# elif mark>=50 and mark<80:
#           print("B")
# elif mark>=50 amd mark<60:
#   prinf("c")
# elif mark >=40 and mark<50:
#   prinf("D")
# else:
#   print("fail")
#---> short hand if else
#     Eg:1
#  a = 94
#    b = 60
# if a>b: 
#  print("A")
# else:
#   print("B")
# ? ---> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) Always it hab]ve to end with else
# print("A") if a>b else print("B")
# le=input("enter the letter")
# print("vowles") if (le=='a' or le=='i' or le=='u' ) else print("consomets")

# str1 = "aeiouAEIOU"
# if char in str1:
#     print("vowel")
# else:
#     print("consonnt")
# ! shorthand if else
# char = input("Enter the char:")
# str1 = "aeiouAEIOU"
# Print("volwes") if chsr in str1 else print("consonent")
# ! ---> elif ladder using short hand else
# Eg:1
# ? find greatest among 3 variables using short hand if else
# a = 8
# b = 5
# c = 9

# print("A is grater") if a>b and a>c else print("B is greater")
# if b>a and b>c else print("c is greater")


# ! ------> looping
# looping can be implimented using
# for loop
# while loop
# -----> for loop

# -----> for loop
# ? for loop is used for iteartion,if we know the number of times the loop have to run
# ? It is used to iterate the iterables eg(string, list, tuple,etc..)

# todo ---> syntax for loop
# ! for syntax for loop
# for(i=0;i<10;i++);
# }

# ! for syntax in python
# for userdefined_variable in range(start, end, step): default setp value is 1
# statement
# statement
# statement

# ? Eg:1

# to print the value from 1 to 10 using for loop



# for i in range(0, 10): # (n ,n-1)
#    # print(i)
#     print("hello")


# ? Eg:2
# for val in range(23, 15, 2):
#   print(val)

# for val in range(23, 15, 3):
#    print(val)


# ? Eg:3
# to decrement the value

# for val in range(10, 0, -2):
    # print(val)

#  for val in range(10, 0, -1):
    # print(val)


# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
# for val in range(1, 10+1):
#    print('7','x',val*7)

# --->   method:2
# ans="7 x{} ={}"
# print(ans.format(val, val*7))


# method:3
#    print(f"7 x {val}={val*7}")

# Eg:5
# break ---> used to teerminate the loop

# for val in range(1, 10):
#    if val ==6:
#      break

#    print(val)

# Eg:6
# for val in range(1, 10):
#     print(val)
#      if val ==6:
#        break

# Eg:7
# for val in range(1, 10):
#        if val ==6:
#        print(val)
#        break


# ! continue
# Eg:1
# for val in range(1,10):
#  if val ==6:
#      continue
#  print(val)

# ! practise problems
# ? print the even number between 20 to 40
# for val in range(20,40):
#     if val&2==0:
#     print(val)
     

# ! practise problems
# ? print the even number between 20 to 40
'''for val in range(20,41):
    if val%2==0:
     print(val)'''
#----> while loop
# while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used

# todo syntax

# initialisation
# while condition:
#    statement
#    incre or decre

#! Eg:1
# to iterate numbedr from 1 to 10

i = 0
while i<11:
    print(i)
    i=i+1 # 0r I+1

i = 10
while i>0:
    print(i)
    i=i-1 # 0r I+1








    

    

    




























      



 


 
