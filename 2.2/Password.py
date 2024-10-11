password = input("enter a password:  ")
# if u enter password, that entered above, script will stop

while True:
    user_input = input ("enter a password to exit a programm  ")
    if user_input == password: 
        print("password is correct, exiting from loop.")
        break
    else:
        print("password is not correct, i wont stop. ")

# if user input = password, script will print: password correct, than break/stop.
# if password wasn't same as entered at first, script will ask to enter password, until password was entered.
# you can use "#" to describe something. script wont read everything on line with #