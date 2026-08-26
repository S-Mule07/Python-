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