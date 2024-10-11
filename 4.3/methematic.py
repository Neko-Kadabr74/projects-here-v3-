import math

def round_up_number(number):
    return math.ceil(number)

def main():
    try:
        user_input = float(input("Please enter a number  ") )
        rounded_number = round_up_number(user_input)
        print(f"wjuuuh! {rounded_number}")
    except ValueError:
        print("hubabuba")

if __name__ == "__main__":
    main()