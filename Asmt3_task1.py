from math import factorial
number = int(input("Enter a Number: "))

def func():
    if number<2:
        return 1
    else:
        return factorial(number)
abc = func()
print(abc)
