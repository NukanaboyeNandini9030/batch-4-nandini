# eg:3
'''def profile(name, age, place):
    txt="my name is {}.Iam{{} years old. Iam from{}."
    print(txt. format(name, age, place))
profile("nandu", 20, "kadapa")'''

# eg:4
# ? function with return statement
# !.)a variable declared inside the function can be accessed outside the function
# using return
#2.)return does not print anything
#3.)we cannot write any code below return statement


# def f1(a, b):
#    c = a*b
#    return c
# print(f1(6, 8))
# obj = f1(6,8)
# obj = f1(4,6)

# def gracemark(object):
#    print(object+4)
#    gracemark(obj)
#    gracemark(obj1)


# 123palindrome
'''def f1(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print("palindrome")
        else: 
            print("not palindrome")
a = int(input("enter the value:"))
palindrome(a)
f1(a)'''


# ? based om the declaration of parameter and args
# ? function are divided into 5 catagories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args


# * positional args
# eg:1
# def profile(name, phone, mark):
#    txt = "my name is {}.my phone number is {}.I got {}marks."
#   print(txt.format(name,phone,mark))
# profile(9090323250, "nandu", 20)# unexpected output

# keyword args
# ! to overcome the disavantages of position args, we use keyword args
# ? it is the process of initialising the paremeter with the args while the args while calling the
# ? function
# def profile(name, phone, mark):
# profile(name="nandu", mark=96, phone=1234567890)
# todo ----> exception of keyword args function
# def profile(name, phone, mark):
#    txt = "my name is {}.my phone number is {}.I got {} marks."
#    print(txt.format(name, phone, mark))
    
# profile(name="nandu", 1234567890, mark=98) # error -> positional args follow keywordargs
# profile(1234567890, name="nandu", mark=98) # error --> name has multiple values
# profile("nandu", mark=98, phone=1234567890)

# default args
# ! eg:1
'''def profile(name, phone, place="kadapa"):
    txt = "my name is {}. my phone number is {}. I am from {} ."
    print(txt.format(name, phone, place))

profile("nandu", 9393933030)'''

# eg:2
'''def profile(name, phone, place="kadapa"):
    txt = "my name is {}. my phone number is {}. I am from {} ."
    if place!="kadapa":
        print("you are not from kadapa")
    else:
        print("kadapa")
        print(txt.format(name, phone, '''  

# eg:2
'''def profile(name, phone, place="kadapa"):
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
        txt = "my name is P{}. my phone number is {} >Iam from {}."
        print(txt. format(name, phone, place))
    else:
        print("you are not eligible to signup")
profile("nandu", 5252909090, "guntur")'''

# ! exception
'''def profile(name,  place="kadapa",phone):
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
        txt = "my name is {}. my phone number is {}.Iam from {}."
        print(txt. format(name, phone, place))
    else:
        print("you are not eligible to signup")
profile("nandu", 5252909090)'''

# * variable length params
# ! eg:1
# to pass more then 1 arg to a paremeter means we use variable length args
# to convert normal paremeter to variable length param,add * to ther prefix of parameter
# name = "sid", 'name2', 'name3'
# def profile(*name):
# print("my name is",name)
# profile("sid", 'name2', 'name3')

# ! eg:2
# def profile(*name,age):
# for val in name:
# print("my name is",val, "may age is", age)
# profile(28,"sid", 'name', 'name3')

# eg:1
# keyword variable length args
'''def price(print_list):
    print(prive_list)

price(shirt=10000,iphone=80000)
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)'''

# #
'''def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
        print(d1)
dict1(5)'''

# ! ----> object oriented programming
# the paradigms of object oriented progarmming are
# class
# objects
# inheritance
# abstraction
# encapsulation
# ! class is a blue print of an object
# l1= [1,2,3,4,5,6,]

# ? eg:1
# class c1:
#      name1 = "sidhu"
#     print(name1)

# ? eg:2
# class person:
# name = "sidhu"

# c = person() # c os object
# the process of creation of an objectn is called as instantiation
# print(c.name)

# ? eg:3
# create of a method
# when the function is created  with a class is as method

# ! method without parameter
# class person:
#    def display():# it is a method
#        print("hello welcome to classes")
# p = person()
# p.display()
# ? method with parameter
# class person:
# def display(person, name, age):
#       print(name, age)

# p= person()
# p.display("sidhu", 28)


# ! eg:5

'''class person1:
    fname = "sidhu" #attribute or static variable
    lname ="t"
    
    def first_name(self):
        print(self.fname)
        
    def full_name(self):
         print(self.fname+" "+person.lname)
p = person1()
p.first_name()
p.full_name()'''

# ? eg:6
# constructors -->_init_()
# class profile:
#    def_init_(self) # construction method
#   print("hey")
#
# p = profile()# execution of construction through this process
# p._init_() 





    

























    
        
    
        
