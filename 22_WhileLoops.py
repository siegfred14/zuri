count = 5

while count > 0:
    print(count)
    count -= 1 # to avoid infinite loops. at count = 1, it subtracts so the result is 0, hence the loop breaks
