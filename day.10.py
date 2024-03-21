# !  method riding
'''class bank:
    def ratio(self):
        print("all bank has repo rate")


class sbi(bank):
    def ratio(self):
        print("sbi rate is 9%")

class iob(bank):
    def ratio(self):
        print(" rate is 7.5%")


i = iob()
i.ratio()

s = sbi()
s.ratio()'''

# ! eg:2
'''class usa:
    def langauge(self):
        print("english")
        def capital(usa):
          def langauge(self):
              print("none")
class india(usa):
    def langauge(self):
        print("none")
        def capital(self):
          print("new delhi")
              
I = india()
I = langauge()
I = capital()'''

# eg:3
# polymorphism  using object

'''class c1:
    def f1(self):
        print("class")
class c2(c1):
    def f1(self):
        print("class")

obj1 = c2()
obj1.f1()

obj2 = c1()
obj2.f1()'''


# ! eg:4
'''class c1:
    def f1(self):
        print("class 1")
class c2:
    def f1(self):
        print("class 2")
obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)'''


# * changing the functionality of buitin function
'''class shooping:
    def__init__(self, l1)
    self.item =l1
    def__len__(self)
    length = len(self.items)
    return length
s = shopping([1,2,3,4,5,])
print(len(s))'''

'''a = 9
b = 6
print(a+b)
print(a.__add__(b)) # ? dunder mettod or mafic method'''
# ! ----> method overloading
# ! eg:1
'''class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
s.add(4, 3) # ! ----> error
s.add(4, 5, 1)'''


# ! eg:2
'''class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
             print(a+b)
        else:
              print(a)
              
obj= summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)'''

# ! -----> abstraction
# the process of hiding the implimentation details us abstraction

# ?eg:1

'''class triangle(shapes):
    def traingle_sides(self):
        print("4 sides")


    def name(self):
        print("Iam triangle")

class square:
    def square(self):
        print("4 sides")
        def sides(self):
         pass
        
tr = triangle()
tr.triangle_sides()
tr.name()'''


# ! rules to define abstract class1

# 1.) Abstract class cannot instantiated
# 2.) from abc import ABC, abstractmethod
# 3.) subclass the normal class with ABC
# 4.) Convert the normal method inside the abstract class to abstract method
# 5.) All the child classes have to be subclassed with abstract class
# 6.) The abstract method should be present in the child classes

# ! eg:2
# super()
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("this is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("iam child 1")
    def m1(self):
         pass
class2 = c2()
class2.m2()


# *eg:3
'''from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "nandu20000$"
        return pswd

class login(password):
    def validata(self, name, password):
        if super().pwd() == password:
            print("welcome", name,'!!')
            print("login  successfully")
        else:
            print("please check the password")
    def pwd(self):
        pass
                


login = login()
name = input("enter the name")
pwd = input("enter the password:")
login.validata(name, pwd)'''


# ! encapsulation
# eg:1
'''class car:
    __name = "BWE" # private variable
    print(__name)

c1 = car()
print(c1.name)# error
c1.name = "Audi"
print(c1.name) # error'''
# ? ----> eg:2
# ? accessing private data the class
'''class c1:
    __phone = '909090909090'

    def display(self):
        print(self.__phone)
c = c1()
c.display()'''

# * -----> eg:3
# ? declare private method
'''class class1:
    def __m1(self): # private method
         print("Iam private method")
    def __init__(self):
        self.__m1()


c = class1()'''

# ? nested class
class class1:
    class class2:
        name = "nandu"

        def display(self):
            print(self.name)
            
    obj1 = class2()
obj = class1()
obj.obj1.display()
    

        

        





























































    

        
