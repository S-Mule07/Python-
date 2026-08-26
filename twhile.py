digit=246
a=1

while digit>0:
    rem=digit%10
    a=a*rem
    digit=digit//10
print("Product of digits =",a)

digit=64
sum=0

while digit>0:
    rem=digit%10
    sum=sum+rem
    digit=digit//10

print("Sum of digits =",sum)

sum=0
i=1

while i<=10:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Total of Even numbers:", sum)

odd=0
i=1

while i<=10:
    if i%2!=0:
        odd=odd+i
    i=i+1
print("Total of Odd numbers:", odd)

z=0

while z<=60:
    print(z)
    z=z+6

i=1

while i<=10:
    square=i*i
    print("Square of", i, "=", square)
    i=i+1

i=1

while i<=10:
    cube=i*i*i
    print("Cube of", i, "=", cube)
    i=i+1

i=1

while i<=10:
    if i%2==0:
        print("Square of", i, "=", i ** 2)
    else:
        print("Cube of", i, "=", i ** 3)

    i=i+1