# Create records
# read record
# update records
# delete record
# Find user
import os
import validation

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
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

        # fetch the content of the file

    except FileNotFoundError:
        print("File Not Found")

    except FileExistsError:
        print("User Doesnt Exist")

    except TypeError:
        print('Invalid Account Number Format')

    else:
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


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        # to read user details and split the string content received into a list
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True

    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(account_number) + ".txt":
            return True

    return False

# create(3440288593, ['Siegfred', 'Samson', 'siegfred@zuri.com', 230])

# delete(5647850565)
# create(5647850565, ["Sam", "Fred", "sam@domo.com", 123456])
# print(read(56478509765))
# print(read(['one', 'two']))
# does_email_exist(3440288593, 'siegfred@zuri.com')
# print(does_email_exist('sam@domo.com'))


print(does_account_number_exist(5470142077))
