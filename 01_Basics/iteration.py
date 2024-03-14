# The enumerate() function is used to iterate over elements in an iterable (such as a list, tuple, or string),
# while keeping track of both the index and the value. 
# It returns an iterator that produces tuples containing the index and the corresponding element.

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# -------- Output --------
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# The zip() function combines multiple iterables (lists, tuples, etc.) element-wise into a single iterable. 
# It returns an iterator of tuples, where each tuple contains elements from the input iterables at the same position.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# -------- Output --------
# Alice: 85
# Bob: 92
# Charlie: 78