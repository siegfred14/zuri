# username = input('What is your username? \n')
# print(username)
#
# allowedUsers = ['Siegfred', 'Kachi', 'Oluchi', 'Ojochide']
# allowedPassword = "Password"
#
# if(username in allowedUsers):
#     password = input("Your Password? \n")
#
#     if(password == allowedPassword):
#         print('Welcome %s' % username);
#     else:
#         print('Password incorrect, Please try again')
# else:
#     print('Name not found. Please Try Again')

    # create form add username and password to list

#     modifying the program to check username and password from list

username = input('What is your username? \n')
print(username)

allowedUsers = ['Siegfred', 'Kachi', 'Oluchi', 'Ojochide']
allowedPassword = ['passSieg', 'passKach', 'passOluchi', 'passChide']

if(username in allowedUsers):
    password = input("Your Password? \n")

    userId = allowedUsers.index(username)

    if(password == allowedPassword[userId]):

        #successful log in
        print('Welcome %s' % username);
        print('These are your available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please Select an Option: \n'))

        balance = 500

        if(selectedOption == 1):
            print('You selected %i' %selectedOption)
            amountToWithdraw = int(input('Enter Amount: \n'))
            if(amountToWithdraw > balance):
                print('Insufficient Balance')
            else:
                balance = balance - amountToWithdraw
                print('Please Take your Cash')
                print('Your Balance is %i' %balance)

        elif(selectedOption == 2):
            print('You selected %i' % selectedOption)
            amountToDeposit = int(input('Enter Amount: \n'))
            balance = balance + amountToDeposit
            print('Transaction Successful')
            print('Your Ledger Balance is %i' %balance)

        elif(selectedOption == 3):
            print('You selected %i' % selectedOption)

        else:
            print('Invalid Selection, Please Try Again')

    else:
        print('Password incorrect, Please try again')
else:
    print('Name not found. Please Try Again')
