# Task 1: Perform Basic Mathematical Operations

# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (Division by Zero)"

# Display results
print("Results:\nAddition: " + str(addition) + 
      "\nSubtraction: " + str(subtraction) + 
      "\nMultiplication: " + str(multiplication) + 
      "\nDivision: " + str(division))
