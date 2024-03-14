# map()
# The map() function applies a given function to each item in an iterable (e.g., list, tuple) and returns an iterator of the results.
# Useful for transforming elements in a collection.

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
# Output: [1, 4, 9, 16]

# filter()
# The filter() function filters elements from an iterable based on a given condition.
# Useful for selecting specific items that meet a certain criterion.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Output: [2, 4, 6]

# reduce() 
# The reduce() function is part of the functools module and is used to apply a particular function 
# to all elements in a sequence (such as a list). 
# It performs a cumulative calculation on the elements, reducing them to a single value.

import functools
numbers = [1, 3, 5, 6, 2]

# Using reduce to find the sum
sum_result = functools.reduce(lambda a, b: a + b, numbers)
print("Sum of the list elements:", sum_result)

# Using reduce to find the maximum element
max_result = functools.reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum element of the list:", max_result)

# Output:
# Sum of the list elements: 17
# Maximum element of the list: 6
