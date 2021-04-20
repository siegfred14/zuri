# Automated Teller Machine Mock Project
from datetime import datetime

username = input('What is your username? \n')
print(username)

allowedUsers = ['Siegfred', 'Kachi', 'Oluchi', 'Ojochide']
allowedPassword = ['passSieg', 'passKach', 'passOluchi', 'passChide']

if username in allowedUsers:
    password = input("Your Password? \n")
    userId = allowedUsers.index(username)
    if password == allowedPassword[userId]:

        # Date and Time added
        abujaDate = datetime.now().strftime("%d/%m/%Y")
        abujaTime = datetime.now().strftime("%H:%M:%S")
        print("Today is ", abujaDate)
        print("Time is ", abujaTime)

        # Salutations and Options
        print('\n Dear %s' % username)
        print('Welcome to Zuri Bank!')
        print('These are your available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please Select an Option: \n'))

        balance = 500

        if selectedOption == 1:
            print('You selected %i' % selectedOption)
            amountToWithdraw = int(input('Enter Amount: \n'))
            if amountToWithdraw > balance:
                print('Insufficient Balance')
            else:
                balance = balance - amountToWithdraw
                print('Please Take your Cash')
                print('Your Balance is %i' % balance)
                print('Thank You For Using Zuri Bank!')

        elif selectedOption == 2:
            print('You selected %i' % selectedOption)
            amountToDeposit = int(input('Enter Amount: \n'))
            balance = balance + amountToDeposit
            print('Transaction Successful')
            print('Your Ledger Balance is %i' % balance)
            print('Thank You For Using Zuri Bank!')

        elif selectedOption == 3:
            print('What Issue Would You Like To Report')
            input('')
            print('\n Thank You For Contacting Us!')

        else:
            print('Invalid Selection, Please Try Again')

    else:
        print('Password incorrect, Please try again')
else:
    print('Name not found. Please Try Again')
