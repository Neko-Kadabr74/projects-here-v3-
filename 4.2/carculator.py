num1 = float(input("Enter the first number:  ") )
num2 = float(input("Enter the second number:  ") )

addition = num1 + num2
substraction = num1 - num2 
multiplication = num1 * num2 
division = num1 / num2 if num2 != 0 else "(undified (division by zero)"

print(f"addition: {addition}")
print(f"substraction: {substraction}")
print(f"multiplication: {multiplication}")
print(f"division: {division}")