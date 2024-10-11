numbers = [26, 1, -1, 10, -10, 10, -10, 90, 98, -305, -20, 0, 9008, 1]

operation = input("choose operation (+, -, *, /): ")
value = float(input("now.. number?: "))

def apply_operation(numbers, operation, value):
    results = []
    for number in numbers:
        if operation == '+':
            results.append(number + value)
        elif operation == '-':
            results.append(number - value)
        elif operation == '*':
            results.append(number * value)
        elif operation == '/':
            if value != 0:
                results.append(number / value)
            else:
                results.append("Cannot / to zero.")
        else:
            return "huh?"
    return results

results = apply_operation(numbers, operation, value)
print("Result:", results)