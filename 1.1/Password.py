password = input("enter a password:  ")

while True:
    user_input = input ("enter a password to exit a programm  ")
    if user_input == password: 
        print("password is correct, exiting from loop.")
        break
    else:
        print("password is not correct, i wont stop. ")