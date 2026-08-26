#if else statement
'''age=20
if(age>=18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#nested if
a=6
if(a>0):
    print("positive number")
if(a%2==0):
    print("even number")

b=5
if(b%2==0):
    print("even number")
else:
    print("odd number")

#user input(runtime)

a=int(input("enter a number:"))
if(a%2==0):
    print("even number")
else:
    print("odd number")

#nested if else
num=int(input("Enter a number:"))
if(num>0):
    print("number is +ve")
    if(num%2==0):
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is -ve")

#ladder if else
x=int(input("Enter a number"))
y=int(input("Enter a number"))
z=int(input("Enter a number"))

if x>y and x>z:
    print("Greater number is :",x)
elif y>x and y>z:
    print("Greater number is :",y)
else :
 print("Greater number is :",z)
    
marks=int(input("Enter marks:"))
if marks>90 and marks<100:
    print("A Grade")
elif marks>70 and marks<90:
    print("B Grade")
elif marks>50 and marks<70:
    print("C Grade")
elif marks>35 and marks<50:
    print("D Grade")
else:
    print("Fail")

#while loop
i=1
while(i<=10):
    print(i)
    i+=1 

num=int(input("Enter number:"))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev) '''

#pallidrome number

num=int(input("Enter a number:"))
rev=0
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse number is:",rev)
if(temp==rev):
    print("Given number is pallidrome number")
else:
    print("Given number is  not pallidrome number")

#armstrong number
num=int(input("Enter a number:"))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=rev+rem**3
    num=num//10
print("Reverse number is:",rev)
if(temp==rev):
    print("Given number is armstrong number")
else:
    print("Given number is  not armstrong number")

 