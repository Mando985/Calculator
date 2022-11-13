import math
import fractions

def calc():
    try:
        num1 = float(input("Enter your first number:\n===>"))
        op = input("Choose your operator: + , - , x , ^ , / , sqrt , log , antilog\n===>")
        if op == "sqrt":
            print(math.sqrt(num1))
        elif op == "log":
            print(math.log10(num1))
        elif op == "antilog":
            print(10 ** num1)
        else:
            num2 = float(input("Enter your second number:\n===>"))
            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "x":
                print(num1 * num2)
            elif op == "^":
                print(num1 ** num2)
            elif op == "/":
                print(num1 / num2)
    except ValueError:
        print("Please enter a number\n")
        calc()
    except ZeroDivisionError:
        print("You cannot divide by zero")

def quad():
    print("ax^2+bx+c")
    a=int(input("Enter number a:\n===>"))
    if a==0:
        print("You cannot have a=0, please try again")
        quad()
    else:
        b = int(input("Enter number b:\n===>"))
        c = int(input("Enter number c:\n===> "))
        D = ((b ** 2) - (4 * a * c))
        if D < 0:
            p = D * -1
            A = fractions.Fraction(str((-b + math.sqrt(D)) / (2 * a)))
            B = fractions.Fraction(str((-b - math.sqrt(D)) / (2 * a)))
            print("The roots of the quadratic equation is", A, "i", "and", B, "i")
            print("The roots of the quadratic equation are imaginary")
        elif D == 0:
            A = fractions.Fraction(str((-b + math.sqrt(D)) / (2 * a)))
            B = fractions.Fraction(str((-b - math.sqrt(D)) / (2 * a)))
            print("The roots of the quadratic equation is", A, "and", B)
            print("The roots of this equation are real and equal")
        elif D > 0:
            A = fractions.Fraction(str((-b + math.sqrt(D)) / (2 * a)))
            B = fractions.Fraction(str((-b - math.sqrt(D)) / (2 * a)))
            print("The roots of the quadratic equation is", A, "and", B)
            print("The roots of this equation are real and distinct")


def area():
    Z = input(
        "Which shape's area would you like to find?\na)Rectangle\nb)Square\nc)Triangle\nd)Circle\ne)Trapezoid\n===>")
    z = Z.lower()
    if z == "a":
        a = float(input("Enter the height:\n"))
        b = float(input("Enter the breadth:\n"))
        print("The area of the shape is ", a * b, "square units")
    elif z == "b":
        a = float(input("Enter the length:\n"))
        print("The area of the shape is ", a ** 2, "square units")
    elif z == "c":
        a = float(input("Enter the first side:\n"))
        b = float(input("Enter the second side:\n"))
        c = float(input("Enter the third side side:\n"))
        y = (a + b + c) / 2
        x = math.sqrt(y * (y - a) * (y - b) * (y - c))
        print("The area of the shape is ", x, "square units")
    elif z == "d":
        a = float(input("Enter the raidus:\n"))
        print("The area of the shape is ", math.pi * (a ** 2), "square units")
    elif z == "e":
        a = float(input("Enter the first side:\n"))
        b = float(input("Enter the second side:\n"))
        c = float(input("Enter the height:\n"))
        print("The area of the shape is ", (a + b) / 2 * c, "square units")


def SA():
    Z = input("Which shape's area would you like to find?\na)Cube\nb)Cuboid\nc)Cylinder\nd)Sphere\ne)cone\n===>")
    z = Z.lower()
    if z == "a":
        a = float(input("Enter the side length:\n"))
        print("The area of the shape is ", 6 * (a ** 2), "square units")
    elif z == "b":
        a = float(input("Enter the length:\n"))
        b = float(input("Enter the breadth:\n"))
        c = float(input("Enter the height:\n"))
        print("The area of the shape is ", 2 * (a * b + b * c + a * c), "square units")
    elif z == "c":
        a = float(input("Enter the radius:\n"))
        b = float(input("Enter the height:\n"))
        print("The area of the shape is ", 2 * math.pi * a * (a + b), "square units")
    elif z == "d":
        a = float(input("Enter the raidus:\n"))
        print("The area of the shape is ", 4 * math.pi * (a ** 2), "square units")
    elif z == "e":
        a = float(input("Enter the radius:\n"))
        b = float(input("Enter the slant height:\n"))
        print("The area of the shape is ", math.pi * a * (a + b), "square units")


def vol():
    Z = input("Which shape's volume would you like to find?\na)Cube\nb)Cuboid\nc)Cylinder\nd)Sphere\ne)cone\n===>")
    z = Z.lower()
    if z == "a":
        a = float(input("Enter the side length:\n"))
        print("The volume of the shape is ", a ** 3, "square units")
    elif z == "b":
        a = float(input("Enter the length:\n"))
        b = float(input("Enter the breadth:\n"))
        c = float(input("Enter the height:\n"))
        print("The volume of the shape is ", a * b * c, "square units")
    elif z == "c":
        a = float(input("Enter the radius:\n"))
        b = float(input("Enter the height:\n"))
        print("The volume of the shape is ", 2 * math.pi * (a ** 2) * b, "square units")
    elif z == "d":
        a = float(input("Enter the raidus:\n"))
        print("The volume of the shape is ", 4 / 3 * math.pi * (a ** 3), "square units")
    elif z == "e":
        a = float(input("Enter the radius:\n"))
        b = float(input("Enter the slant height:\n"))
        print("The volume of the shape is ", 1 / 3 * math.pi * (a ** 2) * b, "square units")


def SA_Vol():
    import math
    Input = input(
        "What would you like to find?\na) Area of a shape\nb) Surface area of a shape\nc)Volume of the shape\n===>")
    Input2 = Input.lower()
    if Input2 == "a":
        area()
    elif Input2 == "b":
        SA()
    elif Input2 == "c":
        vol()

a=input(''' Welcome, which one of the following calculator do you want to run?
A) Arithmetic Calculator
B) Quadratic Equation Solver
C) Area,Total Surface Area or the Volume of the Shape

===>''')
b = a.lower()

if b == "a":
    calc()
elif b=="b":
    quad()
elif b=="c":
    SA_Vol()




