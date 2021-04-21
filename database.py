# Create records
# read record
# update records
# delete record
# Find user


def create(account_number, user_details):
    completion_state = False

    try:
        f = open("data/user_record/" + str(account_number) + ".txt", "x")

    except FileExistsError:
        print('user already exists')
        # delete the already created file and print out error, then return false
        return completion_state

    else:
        f.write(str(user_details))
        completion_state = True

    finally:
        f.close()

    return completion_state

    # create a file
    # name of file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, delete created file


def read(user_account_number):
    print("read user record")
    # find user with account number
    # fetch the content of the file


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_acoount_number):
    print("delete_user record")
    # find user with account number
    # delete the user record(file)
    # return true


def find(user_account_number):
    print('find user')
    # find user record in the data folder


# create(3440288593, ['Siegfred', 'Samson', 'siegfred@zuri.com', 230])

