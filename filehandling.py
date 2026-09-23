f=open("file.txt","r")
print(f.read())
f.close()

f=open("file.txt","r")
print(f.readline(3))

f=open("file.txt","w")
f.write("My document")
f.close()
