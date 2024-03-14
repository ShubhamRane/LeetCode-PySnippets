# Permutations: 
# This refers to all possible arrangements of a set of items, where the order does matter. You can use permutations(iterable, r) to get all possible permutations of length r.
# Combinations: 
# This refers to all possible selections of a set of items, where the order does not matter. You can use combinations(iterable, r) to get all possible combinations of length r.
# Below are examples of how to use these functionalities:
# These snippets will generate all permutations and combinations of length 2 from the list [1, 2, 3]

from itertools import permutations, combinations

# Permutations example
perm = permutations([1, 2, 3])
print(list(perm))
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations([1, 2, 3], r=2)
print(list(perm))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Combinations example
comb = combinations([1, 2, 3], r=2)
print(list(comb))
# Output: [(1, 2), (1, 3), (2, 3)]
