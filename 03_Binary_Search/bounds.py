# Custom implementation

# Lower bound (first occurrence of element greater than or equal to x)
def lower_bound(arr, x):
    """Find the index of the first element in arr that is not less than x."""
    left, right = 0, len(arr)-1
    ans = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans

# Upper bound (first occurrence of an element greater than x)
def upper_bound(arr, x):
    """Find the index of the first element in arr that is greater than x."""
    left, right = 0, len(arr)-1
    ans = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans

arr = [1, 2, 2, 3, 4, 4, 4, 5, 6]
x = 4
print("Lower bound of", x, "is at index", lower_bound(arr, x))
print("Upper bound of", x, "is at index", upper_bound(arr, x))

# Output:
# Lower bound of 4 is at index 4
# Upper bound of 4 is at index 7


# Using bisect module
import bisect

# Lower bound (first occurrence of x)
def lower_bound(arr, x):
    return bisect.bisect_left(arr, x)

# Upper bound (first occurrence of an element greater than x)
def upper_bound(arr, x):
    return bisect.bisect_right(arr, x)

print("Lower bound of", x, "is at index", lower_bound(arr, x))
print("Upper bound of", x, "is at index", upper_bound(arr, x))

# Output:
# Lower bound of 4 is at index 4
# Upper bound of 4 is at index 7