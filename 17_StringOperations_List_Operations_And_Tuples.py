# Converting Number Bases
# from binary to base 10, 0b or 0B then the binary value
# (zero + b or B)
print(0b1110) # Answer is 14

print(0B11) # Answer is 3

# from Octal to Decimal, 0o or 0O then octal value
# (zero + o or O)

print(0o777) # Answer is 511 in decimal

# From Hexadecimal to Decimal. 0x or 0X then octal value
# zero + x or X

print(0x2BCD)


# To find Datatype of a variable
value = 14
print(type(value))

# Strings
# denoted by str in python
print('Siegfred is a Top Computer Programmer')

# String functions
# 1. capitalize() - converts the first character of a string to uppercase

siegfred = 'siegfred is a top computer programmer'
print(siegfred.capitalize())

# 2. casefold() - converts string to lowercase
sam = 'SHE IS BIG'
print(sam.casefold())

# 3. count() - returns the number of times a specific value occurs in a string
print(siegfred.count('e'))

# 4. endswith() - returns true if a string ends with the specified value
print(siegfred.endswith('e')) #false
print(siegfred.endswith('r')) #true

# 5. find() - searches the string for a specified value and returns the position is was found
print(siegfred.find('put'))

