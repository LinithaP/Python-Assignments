'''
12. Create a login page backend to ask users to enter the username and password.
Make sure to ask for a Re-Type Password and if the password is incorrect give a chance to enter it again but it should not be more than 3 times.
'''



def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for _ in range(3):
        retype = input("Re-enter your password: ")
        if retype == password:
            print("Login successful")
            return
        else:
            print("Incorrect password.Try again.")
    print("You have exceeded the maximum number of attempts.")

login()