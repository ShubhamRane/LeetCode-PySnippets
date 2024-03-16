class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Sample tree
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder Traversal:
# Traverse the left subtree, visit the root node, and then traverse the right subtree.
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

print("Inorder Traversal:")
inorder_traversal(root)  # Output: 4 2 5 1 3

# Preorder Traversal:
# Visit the root node, traverse the left subtree, and then traverse the right subtree.
def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

print("\nPreorder Traversal:")
preorder_traversal(root)  # Output: 1 2 4 5 3

# Postorder Traversal:
# Traverse the left subtree, traverse the right subtree, and then visit the root node.
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

print("\nPostorder Traversal:")
postorder_traversal(root)  # Output: 4 5 2 3 1

# Level Order (BFS) Traversal:
# Visit nodes level by level, starting from the root.

from collections import deque
def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("\nLevel Order Traversal:")
level_order_traversal(root)  # Output: 1 2 3 4 5