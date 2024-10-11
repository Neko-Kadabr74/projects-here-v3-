def is_decmail(num):
    try:
        float_num = float(num)
        return '.' in num or 'e' in num.lower()
    except ValueError:
        return False
    
user_input = input("Enter a number:  ")

if is_decmail(user_input):
    print(f"{user_input} is a decmail number.")
else: 
    print(f"{user_input} is not decimal number")