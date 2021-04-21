# user validation 1
def account_number_validation(account_number):
    # check if account number is not empty
    if account_number:

            # ensure account number is an integer by trying to change it to an integer
            try:
                int(account_number)

                if len(str(account_number)) == 10:
                    return True

                else:
                    # print("Account number is a required field")
                    return False

            except ValueError:
                # print('Invalid Account Number, Account Number Should be an Integer')
                return False

            except TypeError:
                # print('Invalid Account Type')
                return False

    else:
        # print('Account number cannot be less or more than 10 digits')
        return False
