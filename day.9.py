# Function to return all uncommon words
'''def UncommonWords(A, B):
    s1=A.split()
    s2=B.split()
    l1=[]
    for i in s1:
        if i not in s2:
            l1.append(i)
    for i in s2:
        if i not in s1:
            l1.append(i)
    l1=list(set(l1))
    return l1
             
 
# Driver Code
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"
 
# Print required answer
print(UncommonWords(s1, s2))'''


'''s1= "Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)'''

# find the 8th fibanochi number
'''num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)'''
#unparametarised constructor
'''class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()'''

# ? parametarised constructor
'''class profile:
    def __init__(self,id,name,age):
        print(id,name,age)

obj = profile(1,"sid",29)'''

# eg:4

# m1
'''class c1:
    name="nandu"
    place="kad"
    def m1(self):
        print(self.name,self.place)
obj=c1()
obj.m1()'''
#m2
'''class c1:
    def m1(self):
         name="nandu"
         place="kad"
         print(name,place)
obj=c1()
obj.m1()'''
#m3
'''class c1:
    email="nandu@gmail.com"
    def m1(self):
         name="nandu"
         place="kad"
         print(name,place)
         print(self.email)
obj=c1()
obj.m1()'''
#ex5
'''class c1:
    def  m1(self):
         name="nandu"
         place="kad"
         return name,place
    def display(self):
        print(self.m1())
obj=c1()
obj.display()'''
# eg:6
'''class class1:
    def__init__(self):
        name = "sid"
        email = "sid@gmail.com"
        # return name, email # error
      def display(self):
          priny(self.name, self.email)
          
c1 = class()
c1.display()'''








# ! ------> Inheritance
# the process of utilising the method and attributes of parent class
# through the object of child class if is called as inheritance



# ! eg:1
'''class parent:
    def m1(self):
        print("iam parent class")
class child(parent):
    def m2(self):
        print("iam child class")
obj = child()
obj.m1()'''

# ! eg:2

'''class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child(c1):
    pass

obj = child()'''


# eg:3
'''class parent:
    name ="sidhu"
    
class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()'''


# ! muttilevel inheritance
'''class voice:
    def sound(self):
        print("all the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
                
class cat(dog):
    def cat_voice(self):
        print("meow")
class parrot(cat):
    def parrot_voice(self):
        print("speak")
                    
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()'''

# eg:2
# ! multiple Inheritance
# it has multiple parent and 1 child
'''class while_petrol:
    def function_w(self):
        print("used for airplans")
        
class organic_petrol:
    def function_p(self):
        print("spots cars, bikes")
        

class organic_petrol:
    def function_o(self):
        print("spots cars, bikes")
        
class petrol(while_pertol, organic_petrol, premium_petrol):
    def defanitional(self):
        print("petrols types")
        
p = petrol()
p.defanition()
p.function()
p.function()'''

# eg:3
# MRO---> Method resolution Order
'''class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)'''

# ! heirarical inheritance

'''class category:
    def weight_name(self):
        print("weight")
        
     def display(self, color, taste):
         print(colour, taste)
        
class tomoto(catagory):
     def tomato_specs(self):
         colour="black"
         taste = "neutral taste"
         self.display(colour. taste)
         print(weight)
         
class carrot(catagory):
    def carrot_specs(self):
        colour="black"
        taste = "neutral taste"
        self.display(colour, taste)
t = tomoto()
t.tomoto_specs()
t.weight("20")'''

# ! hybrid inheritance
# ? the combination of above 4 inheritance is called hybrid inheritance
'''class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("class3")
class c4(c2):
    def m4(self):
        print("class 3")
        
class c5(c3):
    def m5(self):
        print("class 4")
        
class c6(c5,c3):
    def m6(self):
        print("class 4")
obj = c6()
obj.m3()'''

# ! -------> polymorphism

# poly - many, morph ---> form
# ? a function which has ability to perform more than 1 functionality
# then it is considered to be as polimorphism


# * ploymorphism in builtin function
# len() --> whivh is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()# and more...

# * ploymorphism in operators
# +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[5,6])

# *
# print(6*7)
# l1 = {1,2,3,4,5,6}
# print(*l1)
# def f1(*args)
# l1 = [1,2,3,4]
# print(l1*10)


# ploymorphism in classes
# we can achieve polymorphism in 2 ways
# 1.) method overloading ----> if is not possible in python
# 2.) method overriding

#1.) tasks

# d1 ={"shirt": 1000, "pant": 1500, "shoes": "900", "handkey": 30}
# 1.) find the min ans max priced product
# 2.) find the product starts with 's' and 's'

      
     















                    



                    
                    

        


    

        





















 
              

















