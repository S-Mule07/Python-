'''#non parametrized function

def wish():
    print("Hello")
wish()
print("bye")
wish()

#parametrized function

def add(a,b):
    print("Sum:",a+b)
add(10,20)
add(20,50)

#return statement

def add(x,y):
    return x+y
print("Addition:",add(10,20))

#required argument
def display(name):
    print("My name is",name)
display("Samrudhi")

#keyword argument

#default 
def info(name,age,city="Pune"):
    print(name,age,city)
info("Samu",19)
info("Nikita",20,"Mumbai")

#palindrome number

def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if palindrome(n):
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")

#armstrong

def armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if armstrong(n):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")'''

#variable length argument

def hello(name,*marks):
    print("Name=",name)
    print("Marks=",marks)
hello("Samu",90,80,95)

#keyword length argument= pass all the values in form of dictionary inside **mark parameter

def hello(name,**marks):
    print("Name=",name)
    print("Marks=",marks)
hello("Samu",M=90,N=80,O=95)

#lambda function

sum=lambda x,y:x+y
Total=sum(10,20)
print(Total)

cube=lambda x:x*x*x
Total=cube(2)
print(Total)