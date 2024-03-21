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





























































    

        
