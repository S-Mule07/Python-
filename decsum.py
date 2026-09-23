def decore(func):

    def inner(num3):
        result = func(num1, num2)

        print("Num3 is:", num3)
        print("Result + Num3 =", result + num3)

    return inner


@decore
def number(num1, num2):
    result = num1 + num2
    print("The addition of the numbers is:", result)
    return result


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

number(num3)