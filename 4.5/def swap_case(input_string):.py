def swap_case(input_string):
    return input_string.swapcase()

def main():
    user_input = input("Enter a string:  ")
    swapped_string = swap_case(user_input)
    print("Swap!", swapped_string)

if __name__ == "__main__":
    main()
