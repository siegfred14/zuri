
a_list = [1, 2, 3, 4, 5, 6]

# forLoops
for item in a_list:
    print(item)

print('========')
for x in range(6):
    print(x)

print('========')

# combine for and if
for x in range(6):
    if x != 0:
        print(x)

print('========')

# or
for x in range(6):
    if not(x == 0):
        print(x)

# iterating a list
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    result = i * 'X'
    print(result)

for i in numbers:
    result = ''
    for j in range(i):
        result += 'X'
    print(result)

# getting the largest number in a sequence
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item
print(largest)
