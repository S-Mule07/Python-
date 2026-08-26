#for loop

for i in range(0,11):    #start from 0 end with 11-1=10
    print(i)

for a in range(0,11,2):  #start,stop,step
    print(a)

for b in range(11,0,-1):
    print(b)

for c in range(0,11,2):
    print(c)

for d in range(1,11,2):
    print(d)

sum=0
for i in range(1,11):
        if i%2==0:
         sum=sum+i
print(" Total of Even numbers:",sum)

odd=0
for i in range(1,11):
    if i%2!=0:
        odd=odd+i
print(" Total of Odd numbers:",odd)

for z in range(0,61,6):
    print(z)

for i in range(1, 11):
    square = i * i
    print("Square of", i, "=", square)

for i in range(1, 11):
    cube = i * i * i
    print("Cube of", i, "=", cube)

for i in range(1, 11):
    if i % 2 == 0:
        print("Square of", i, "=", i ** 2)
    else:
        print("Cube of", i, "=", i ** 3)





