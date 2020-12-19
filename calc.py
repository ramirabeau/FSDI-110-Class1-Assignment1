# Have user input two numbers and perform
# addition, subtraction, multiplication, and division
# with those two numbers


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def clear():
    print("\n\n\n")


clear()
print("Select your mathmatical operation.")

print("1.  Addition")
print("2.  Subtraction")
print("3.  Multiplication")
print("4.  Division")
opr = int(input("Enter your Selection (1/2/3/4):  "))
if (opr < 1 or opr > 4):
    print("You have made an invalid selection, choose another selection.")
else:
    num1 = int(input("Enter your first number:  "))
    num2 = int(input("Enter your second number:  "))
    if (opr == 1):
        print(num1, " + ", num2, " = ", addition(num1, num2))
    elif (opr == 2):
        print(num1, " - ", num2, " = ", subtraction(num1, num2))
    elif (opr == 3):
        print(num1, " * ", num2, " = ", multiplication(num1, num2))
    elif (opr == 4):
        if (num2 != 0):
            print(num1, " / ", num2, " = ", division(num1, num2))
        else:
            print("You cannot divide by zero.")

clear()
