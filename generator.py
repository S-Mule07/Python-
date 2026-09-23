def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g=mygen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))

def countdown(num):
    print("start countdown")
    while(num>0):
        yield num
        num=num-1

value=countdown(5)
for x in values:
    print(x)