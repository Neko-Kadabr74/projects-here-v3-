def main():
    while True:
     try:
         number = float(input("enter a number, cheese.") )
         if number < 0: 
            print("number is negative. but not evil.")
         elif number >0:
            print("number is positive, but not kind.")
         else:
            print("this number is both positive and negative.")
            break
     except ValueError:
         print("I need number, not words.")

if __name__ == "__main__":
    main()