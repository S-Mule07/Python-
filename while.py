i=1
while(i<=10):
    print(i)
    i+=1

i=10
while(i>=1):
    print(i)
    i-=1

num=int(input("Enter number:"))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse number is:",rev)