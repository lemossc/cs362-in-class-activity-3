# Author: Christopher LeMoss
# Date: February 4, 2021
# Description: In-Class-Activity 3 - Unit Testing
#   for CS362 Software Engineering II at Oregon State University.
# Assignment Instructions:
# 1. Write tests for a simple calculator app.
# 2. Your app should take two numbers as inputs (a,b).
# 3. Should have the following methods: addition, subtraction, multiplication, division.
# 4. Create a test module that has your test cases.


def addition(a, b):
    if is_number(a) and is_number(b):
        return a + b
    else:
        return None


def subtraction(a, b):
    if is_number(a) and is_number(b):
        return a - b
    else:
        return None


def multiplication(a, b):
    if is_number(a) and is_number(b):
        return a * b
    else:
        return None


def division(a, b):
    if is_number(a) and is_number(b) and b != 0:
        return a / b
    else:
        return None


def is_number(value):
    if isinstance(value, int) or isinstance(value, float):
        return True
    else:
        return False


def calculator_loop():
    while True:
        user_input = ""
        a = 0
        b = 0
        try:
            user_input = input("Enter operand 'a' (or type 'q' to exit): ")
            if user_input[0] == "q":
                break
            else:
                a = float(user_input)
            b = float(input("Enter operand 'b': "))
        except ValueError:
            print("Error: 'a' and 'b' must be numbers")
            continue

        operation = input("Enter an operation ('+', '-', '*', or '/')")
        result = None
        if operation == "+":
            result = addition(a, b)
        elif operation == "-":
            result = subtraction(a, b)
        elif operation == "*":
            result = multiplication(a, b)
        elif operation == "/":
            result = division(a, b)
        else:
            print("Error: Second argument must be '+', '-', '*', or '/'")
            continue
        if result is None:
            print("Error: 'a' and 'b' must be numbers (and cannot divide by 0)")
        else:
            print(a, " ", operation, " ", b, " = ", result)
        print()
