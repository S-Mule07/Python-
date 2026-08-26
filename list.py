numbers = [10, 20, 30, 40, 50]
print(numbers[0:3])

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:6])

fruits = ["Apple","Banana","Mango","Orange"]
print(fruits[:])

colors = ["Red","Blue","Green","Yellow","Black"]
print(colors[:4])

names = ["Amit","Rahul","Sneha","Priya","Neha"]
print(names[2:])

numbers = [10, 20, 30, 40, 50]
print(numbers[-3:])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:8:2])

fruits = ["Apple","Banana","Mango","Orange","Grapes","Kiwi"]
print(fruits[::2])

numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[4:1:-1])

#methods and functions

fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

fruits = ["Apple", "Banana"]
fruits.extend(["Mango", "Orange"])
print(fruits)

numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)

numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)

fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Mango"))

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

numbers = [10, 20, 30, 40, 50]
print(len(numbers))

numbers = [10, 50, 20, 40, 30]
print(max(numbers))

numbers = [10, 50, 20, 40, 30]
print(min(numbers))

numbers = [10, 20, 30, 40]
print(sum(numbers))

numbers = [50, 20, 40, 10, 30]
new_list = sorted(numbers)
print(new_list)

