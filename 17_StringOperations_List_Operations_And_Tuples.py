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

# 6. isalpha() - returns true if all characters in the string are alphabets
print(sam.isalpha()) # false because of the space in between

kachi = 'elizabeth'
print(kachi.isalpha()) #true

# 7. isalnum() - returns true if all characters in the string are alphanumeric
print(sam.isalnum()) # false

kachi = 'elizabeth23'
print(kachi.isalnum()) # true

# 8. isalpha() - returns true if all characters in the string are alphabets
# 9. isdecimal() - returns true if all characters in the string are decimal
# 10. isdigit() - returns true if all characters in the string are digits

# 11. replace() - returns a string where a specified value is replaced with a specified value
print(siegfred.replace('e', 'o'))
print(siegfred.replace('siegfred', 'SIEGfRed'))

# 12. upper() converts a string into uppercase
# 13. lower() converts a string into lowercase

