# register
# - first name, last name, password and email
# - generate userAccount

# login
# - account number and password

# bank operations

# Initializing the system
import random
import database
import validation


# dictionary


def init():
    print('Welcome to Zuri Bank')

    have_account = int(input('Do you have an account with us? 1 (Yes) 2(No) \n'))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You Have selected an invalid option')
        init()


def login():
    print("******* Login *******")

    account_number_from_user = (input("What is Your Account Number? \n"))
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input('Input Your Password \n')

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operation(user_details)

        print('Invalid Account or Password')
        login()

    else:
        init()


def register():
    print("******Register*****")

    email = input('What is Your email Address? \n')
    first_name = input('What is Your First Name \n')
    last_name = input('What is Your Last Name \n')
    password = input("Create A Password For Yourself \n")

    account_number = generating_account_number()

    database[account_number] = [ first_name, last_name, email, password] # This creates a key in th dictionary database and adds the first_name et-al as values

    print(f"Your Account {account_number} has been successfully created")

    login()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))
    if selected_option == 1:
        deposit_operation()

    elif selected_option == 2:
        withdrawal_operation()

    elif selected_option == 3:
        login()

    elif selected_option == 4:
        exit()

    else:
        print("Invalid Option Selected")
        bank_operation(user)


def withdrawal_operation():
    print('Withdrawal')


def deposit_operation():
    print('Deposit Operation')


def generating_account_number():
    return random.randrange(1111111111, 9999999999) # to give a random number within 10 digits


def logout():
    login()


# ACTUAL BANKING SYSTEM ####

init()
