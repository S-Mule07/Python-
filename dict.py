d=dict()
print(type(d))    #empty dictionary

s=set()
print(type(s))    #empty set

d={1:'abc',2:'lmn',3:'pqr',4:'lmn'}

#print a dictionary
print(d)

#accessing values using keys
print("1st name is"+d[1])
print("2nd name is"+d[4])

print(d.keys())
print(d.values())

s={2,1,3,5,2,3,6,1,3,4}    #set
print(s)                    #printing set values

s.add(10)     #adding element
print(s)

s.remove(2)   #removing element
print(s)

#intersection_update()

#task
students = {}
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter student name: ")
    marks=float(input("Enter student marks: "))
    students[name]=marks

print("\nStudent Dictionary:")
print(students)
