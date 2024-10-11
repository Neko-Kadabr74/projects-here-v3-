def main():
    while True:
        try:
            num1 = float(input("Enter a first number..  ") ) 
            num2 = float(input("Enter a second number..  ") )

            result = num1 * num2
            print(f"result:{result}")

            if result > 0:
                print("Positive result, would be hot, maybe..")
            elif result < 0:
                print("negative, pretty cold, i'm sure")
            else:
                print("it's zero")
            
            break

        except ValueError:
            print("Oh, so.. you like to substract 5 liters from january 38?, now try again, i won't stop until i get a number ")

if __name__ == "__main__":
    main()