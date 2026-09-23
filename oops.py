#OOPS

class student:
    def __init__(self):
        self.name="Samrudhi"
        self.age=19
        self.marks=90

    def display(self):
        print("Name of student is",self.name)
        print("Age of student is",self.age)
        print("Marks of student is",self.marks)

s1=student()
s1.display()

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("Name of student is",self.name)
        print("Age of student is",self.age)
        print("Marks of student is",self.marks)

s1=student("Samu",20,80)
s1.display()