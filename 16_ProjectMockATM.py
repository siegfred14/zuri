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
        print('Welcome %s' % username);
    else:
        print('Password incorrect, Please try again')
else:
    print('Name not found. Please Try Again')
