#local variable: access only in the block of function

def student():
    samu="Heloo"   #samu local variable
    print(samu)
student()

#global variable: access to all function block declared outside function

v="Virat"         #virat global variable
def a():
    print(v)
a()
def b():
    print(v)
b()

#if we want to declare a global variable inside a function block use "global" keyword

v="Virat"         #virat global variable
def a():
    global c
    c="India"
    print(v)
a()
def b():
    print(v)
    print(c)
b()
