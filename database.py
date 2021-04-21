# Create records
# read record
# update records
# delete record
# Find user
import os

user_db_path = "data/user_record/"


def create(user_account_number, user_details):
    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        print('User already exists')
        # delete the already created file and print out error, then return false

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
    # find user with account number
    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "r")
        # fetch the content of the file

    except FileNotFoundError:
        print("File Not Found")

    except FileExistsError:
        print("User Doesnt Exist")

    finally:
        return f.readline()


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_account_number):
    # find user with account number
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            print("User Not Found")

        finally:
            return is_delete_successful
    # delete the user record(file)
    # return true


def find(user_account_number):
    print('find user')
    # find user record in the data folder


# create(3440288593, ['Siegfred', 'Samson', 'siegfred@zuri.com', 230])

# delete(5647850565)
# create(5647850565, ["Sam", "Fred", "sam@domo.com", 123456])
print(read(56478509765))