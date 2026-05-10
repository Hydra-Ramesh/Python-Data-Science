#PRD : Simple Calculator (Version 1.0)
"""
1. Two numbers are taken from the user.
2. We will perform basic arithmatic operations (addition, subtraction, multiplication, division, modulus, exponentiation, floor division) on these numbers and display the results.
3. We will give responses to the user.
"""
# System Design:
# 1. Input: Take two numbers as input from the user and type will be float to allow decimal numbers.
# 2. Processing: Perform the following operations on the input numbers:
#    a. Addition (a + b)
#    b. Subtraction (a - b)
#    c. Multiplication (a * b)
#    d. Division (a / b)
#    e. Modulus (a % b)
#    f. Exponentiation (a ** b)
#    g. Floor Division (a // b)
# 3. Output: Display the results of all the operations to the user.


# Step 1: Input
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

# Step 2: Processing
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
modulus=num1%num2
exponentiation=num1**num2
floor_division=num1//num2

# Step 3: Output
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
print(f"Floor Division: {floor_division}")

