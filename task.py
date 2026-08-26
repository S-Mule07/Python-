marks = 75
if(marks>50):
    print("You passed the exam")
else:
    print("you failed")

num = int(input("Enter a number: "))
if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

num = int(input("Enter a number: "))
if num>=0:
    print("Number is Positive")
else:
    print("Number is Negative")

num = int(input("Enter a number: "))
if num%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

age = int(input("Enter your age: "))
if age>=18:
    print("You are an Adult")
else:
    print("You are a Minor")

cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))
if sp > cp:
    print("There is a Profit")
else:
    print("There is a Loss")

num = int(input("Enter a number: "))

if num==10:
    print("Number is 10")
else:
    print("Number is not 10")

temp = int(input("Enter temperature: "))
if temp>30:
    print("It is Hot")
else:
    print("It is Cool")

num = int(input("Enter a number: "))
if num%2==0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2")

password = input("Enter password: ")
if password=="12345":
    print("Login Successful")
else:
    print("Incorrect Password")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
else:
    print("B is greater")

#nested if else
num = int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")

num=int(input("Enter a number: "))
if num>10:
    if num%2==0:
        print("Number is greater than 10 and even")
    else:
        print("Number is greater than 10 and odd")
else:
    print("Number is not greater than 10")

username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin":
    if password=="1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

temp=int(input("Enter temperature: "))
if temp>30:
    if temp>40:
        print("Very hot")
    else:
        print("Hot")
else:
    print("Temperature is normal")

attendance=int(input("Enter attendance percentage: "))
marks=int(input("Enter internal marks: "))
if attendance>=75:
    if marks>=40:
        print("Student is eligible for exam")
    else:
        print("Student is not eligible due to low marks")
else:
    print("Student is not eligible due to low attendance")

#ladder if else
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

num = int(input("Enter a number: "))
if num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

temp = int(input("Enter temperature: "))
if temp >= 40:
    print("Very Hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Normal")
elif temp >= 10:
    print("Cold")
else:
    print("Very Cold")

day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

ch = input("Enter an alphabet: ")
if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")



