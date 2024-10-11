def main():
    while True:
     try: 
         number = float(input("Enter a number. please.. >.>"): "")
         if number == 0:
            print("this number is equal to zero. :0")
     
         else:
            print("this number is diffrent from zero ;|")
     except ValueError:
        print("Words are not numbers.")
if __name__ == "__main__":
    main()