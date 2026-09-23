a=int(input("Enter first value:"))           #runtime error
b=int(input("Enter second value:"))
c=a/b
print(c)

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x,y)
except ZeroDivisionError:
    print("Can't Divide withZero")
except ValueError:
    print("Please provide int value only")


try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")

try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("Outer except block")
finally: 
    print("Outer finally block")