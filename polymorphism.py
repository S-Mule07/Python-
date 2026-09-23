#method overloading
class test:
    def wish(self):
        print("Hello")

    def wish(self,a):
        print("Good morning")

    def wish(self,a,b):
        print("Good night")

t=test()
t.wish(1,2)

#default arguments
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of 3 numbers is",a+b+c)
        elif a!=None and  b!=None:
            print("The sum of 2 numbers is",a+b)
        else:
            print("PLease provide 2 or 3 arguments")

t=Test()
t.sum(10,20,30)

#method overriding
class P:
    def property(self):
        print("Gold+Land")
    def marry(self):
        print("Samrudhi")
class C(P):
    def marry(self):
        print("Yz")

c=C()
c.property()
c.marry()

#super() method

class P:
    def property(self):
        print("Gold+Land")
    def marry(self):
        print("Samrudhi")
class C(P):
    def marry(self):
        super().marry()
        print("Yz")

c=C()
c.property()
c.marry()

#constructor overriding

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee(person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno 
        self.esal=esal

def display(self):
    print("Employee name",self.name)
    print("Employee age",self.age)
    print("Emplyee no",self.eno)
    print("Employee salary",self.esal)

e1=employee("Durga",24,101,15000)
e1.display()
