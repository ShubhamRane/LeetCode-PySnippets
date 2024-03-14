# Bitwise AND, OR, and XOR:
# These operators (&, |, ^) manipulate individual bits of integers.
# Example:

a = 5  # 101 in binary
b = 3  # 011 in binary

# Bitwise AND
result_and = a & b  # 001 (1 in decimal)

# Bitwise OR
result_or = a | b  # 111 (7 in decimal)

# Bitwise XOR
result_xor = a ^ b  # 110 (6 in decimal)

# Checking if a Number is a Power of Two:
# A number is a power of two if it has only one bit set (i.e., it is of the form 2^n).
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Counting Set Bits (Hamming Weight):
# The number of set bits (1s) in an integer.
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Checking the nth Bit:
# To check if the nth bit of an integer num is set (i.e., equal to 1), we can use the bitwise AND operation with a mask that has only the nth bit set.
def is_nth_bit_set(num, n):
    mask = 1 << n
    return (num & mask) != 0

# Setting the nth Bit:
# To set the nth bit of an integer num to 1, we can use the bitwise OR operation with a mask that has only the nth bit set.
def set_nth_bit(num, n):
    mask = 1 << n
    return num | mask

# Flipping Bits:
# Inverting all bits of an integer.
def flip_bits(n):
    return ~n

# Checking if a Number is Even or Odd:
# The least significant bit (LSB) of an odd number is 1.
def is_even(n):
    return n & 1 == 0

# Swapping Two Numbers:
# Using XOR to swap values without using a temporary variable.
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Finding the Single Number:
# Given an array where every element appears twice except for one, find that single number.
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result