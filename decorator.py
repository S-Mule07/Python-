def decor(func):                #applying decorator
    def inner(name):
        if name=="Niky":
            print("Hello",name ,"Shut up")
        else:
            func(name)
    return inner

@decor

def wish(name):              #normal function
    print("Hello",name,"Good morning")
wish("Samu")
wish("Niky")
wish("Mehek")

def decor(func):                #without using @decor
    def inner(name):
        if name=="Niky":
            print("Hello",name,"Shut up")
        else:
            func(name)
    return inner


def wish(name):              #normal function
    print("Hello",name,"Good morning")
decorfunction=decor(wish)

wish("Niky")
wish("Samu")

decorfunction("Niky")
decorfunction("Samu")


def sum(num):
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    num3=int(input("Enter a number:"))
    result=num1+num2+num3
    print("Sum=",result)
sum(3)