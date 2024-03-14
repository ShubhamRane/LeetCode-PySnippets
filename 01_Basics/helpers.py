# The Counter class from the collections module is a subclass of dict that helps to count hashable objects. It’s a convenient way to create histograms and count occurrences of elements in Python.
# Here’s an example of how to use the Counter class:

from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print(word_counts)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})