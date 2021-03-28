username = input('What is your username? \n')
print(username)

allowedUsers = ['Siegfred', 'Kachi', 'Oluchi', 'Ojochide']
allowedPassword = "Password"

if(username in allowedUsers):
    password = input("Your Password? \n")

    if(password == allowedPassword):
        print('Welcome %s' % username);
    else:
        print('Password incorrect, Please try again')
else:
    print('Name not found. Please Try Again')

    # create form add username and password to list

