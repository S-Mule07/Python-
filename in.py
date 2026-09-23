#single
class animal:
   def speak(self):
      print("Animal speaking")
#child class dog inherits the base class animal

class Dog(animal):
   def bark(self):
      print("Dog barking")
d=Dog()
d.bark()
d.speak()


#multilevel


class animal:                    #grandfather
   def speak(self):
      print("Animal speaking")

#child class dog inherits the base class animal

class Dog(animal):            #father
   def bark(self):
      print("Dog barking")

#the child class dogchild inherits another child class dog

class dogchild(Dog):          #child
   def eat(self):
      print("Eating bread")
d=dogchild()
d.bark()
d.speak()
d.eat()

#multiple

class calculation1:
   def summation(self,a,b):
      return a+b;
class calculation2:
   def multiplication(self,a,b):
      return a*b;
class Derived(calculation1,calculation2):
   def divide(self,a,b):
      return a/b;
d=Derived()
print(d.summation(10,20))
print(d.multiplication(34,21))
print(d.divide(30,2))

#hierarchical          single parent multiple child

class animal:                    
   def eat(self):
      print("Animal can eat")


class Dog(animal):           
   def bark(self):
      print("Dog barks")

class cat(animal):
   def meow(self):
      print("Cat meows")

d=Dog()
d.eat()
d.bark()

c=cat()
c.eat()
c.meow()

#Hybrid         mix of hierarchical and multiple

class animal:                    
   def eat(self):
    print("Animal can eat")


class Dog(animal):           
   def bark(self):
    print("Dog barks")

class cat(animal):
   def meow(self):
    print("Cat meows")

class Pet(Dog,cat):
   def play(self):
    print("Pet plays")

p=Pet()
p.eat()
p.bark()
p.meow()
p.play()