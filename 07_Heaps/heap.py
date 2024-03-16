# Note: You need not necessarily have a separate class during interviews.
# This is meant for revision purposes, so you know the available functions to use

import heapq

class MinHeap():
    def __init__(self, items = list()):
        self.heap = items.copy()
        heapq.heapify(self.heap)
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

minHeap = MinHeap()
minHeap.push(8)
minHeap.push(4)
minHeap.push(12)
minHeap.push(1)

print("MinHeap Output:")
print(minHeap.pop(), end = " ")
print(minHeap.pop(), end = " ")
print(minHeap.pop(), end = " ")
print(minHeap.pop(), end = " ")
print()
# MinHeap Output:
# 1 4 8 12


# heapq is by default a min heap. You need to make some adjustments for creating a max heap.
class MaxHeap():
    def __init__(self):
        self.heap = list()
    
    def push(self, item):
        heapq.heappush(self.heap, -item) # insert negative
    
    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

maxHeap = MaxHeap()
maxHeap.push(8)
maxHeap.push(4)
maxHeap.push(12)
maxHeap.push(1)

print("MaxHeap Output:")
print(maxHeap.pop(), end = " ")
print(maxHeap.pop(), end = " ")
print(maxHeap.pop(), end = " ")
print(maxHeap.pop(), end = " ")

# MaxHeap Output:
# 12 8 4 1