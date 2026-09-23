#public variable
class fortune:
    wifi=""
    contact=0


    def __init__(self):
        self.wifi="Student5g"           #public variable
        self.contact=7620691288

        
f=fortune()

print(f.wifi)
print(f.contact)


#protected

class parent:
    def __init__(self):
        self._money=500

class child(parent):
    def display(self):
        print(self._money)

c=child()
c.display()

#private method

class rectangle:
    __length =0 #private variable
    __breadth =0 #private variable

    def __init__(self):
        self.__length=5
        self.__breadth=3

        print(self.__length)
        print(self.__breadth)

rec=rectangle()

#protected

class shape: #protected variable
    _length=10
    _breadth=20

class circle(shape):
    def __init__(self):
        print(self._length)
        print(self._breadth)

c=circle()