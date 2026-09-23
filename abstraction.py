from abc import ABC , abstractmethod

class car(ABC):

    @abstractmethod
    def speed(self):
        pass

class Defender(car):
    def speed(self):
        print("Defender speed is 191 km/h")
class Mercedes(car):
    def speed(self):
        print("Mercedes speed is 150 km/h")
class BMW(car):
    def speed(self):
        print("BMW speed is 200 km/h")
class Fortuner(car):
    def speed(self):
        print("Fortuner speed is 250 km/h")

d=Defender()
d.speed()

m=Mercedes()
m.speed()

b=BMW()
b.speed()

f=Fortuner()
f.speed()

