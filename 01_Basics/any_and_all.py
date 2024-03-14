# any() and all()
# The any() function returns True if at least one element in an iterable is True.
# The all() function returns True if all elements in an iterable are True.
# Useful for checking conditions across multiple elements.
# These are very useful in recursion

values = [True, False, True]
print(any(values))  # Output: True
print(all(values))  # Output: False

fruit_color_tuples = [
    ('Apple', 'Red'),
    ('Banana', 'Yellow'),
    ('Orange', 'Orange'),
    ('Grapes', 'Purple'),
    ('Watermelon', 'Green and Red'),
    ('Blueberry', 'Blue'),
    ('Strawberry', 'Red'),
    ('Kiwi', 'Brown and Green'),
    ('Pineapple', 'Yellow and Brown'),
    ('Cherry', 'Red')
]

# Check if any fruit is Yellow
print(any(color == "Yellow" for _, color in fruit_color_tuples)) # Output: True

# Check if all fruits are Yellow
print(all(color == "Yellow" for _, color in fruit_color_tuples)) # Output: False