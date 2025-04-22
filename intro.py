import math

name = "Benjamin Mintz"


def print_name(name):
    print(name)
    return 0

def adder(a, b):
    return a + b

def area (a):
    return math.pi * (a ** 2)
if __name__ == "__main__":
    name = input("What is your name?: ")
    print_name(name)
    a = int(input("Please give me a number: "))
    b = int(input("Can I have one more number: "))
    print("Sum:", adder(a, b))
    rad = float(input("What is the radius of a circle you'd like the area to: "))
    print("Area: ", area(rad))