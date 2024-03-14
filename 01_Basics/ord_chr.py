# ord() Function:
# The ord() function converts a character into an integer representing its Unicode code point value.

# Convert ASCII Unicode Character 'A' to 65
y = ord('A')
print(type(y), y)  # Output: <class 'int'> 65

# Print Unicode code points for A-Z
alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in alphabet_list:
    print(ord(char), end=", ")  # Output: 65, 66, 67, ..., 90

# chr() Function:
# The chr() function converts a Unicode code character into the corresponding string.

# Convert integer 65 to ASCII Character ('A')
y = chr(65)
print(type(y), y)  # Output: <class 'str'> A

# Print characters for Unicode code points 65-90
for i in range(65, 91):
    print(chr(i), end=", ")  # Output: A, B, C, ..., Z