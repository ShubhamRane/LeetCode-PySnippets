class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print("Stack Output:")
print(s.pop(), end=" ")
print(s.pop(), end=" ")
print(s.pop(), end=" ")
# Stack Output:
# 3 2 1