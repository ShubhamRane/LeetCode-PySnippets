from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, n):
        self.queue.append(n)
    
    def dequeue(self) -> int:
        if self.queue:
            return self.queue.popleft()
        return None

# Example usage
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue Output:")
print(q.dequeue(), end=" ")
print(q.dequeue(), end=" ")
print(q.dequeue(), end=" ")
# Queue Output:
# 1 2 3