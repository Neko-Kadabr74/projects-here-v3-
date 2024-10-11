input_numbers = input("enter 2 numbers: ")
num1, num2 = map(int, input_numbers.split())

if num1 <= num2:
    numbers = range(num1, num2 + 1)
else:
    numbers = range(num2, num1 + 1)

print(", ".join(map(str, numbers)))