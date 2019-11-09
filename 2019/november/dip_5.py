#%% [markdown]
# You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.
#
# Example
# Input:
#     a
#    / \
#   b   c
#  / \  /
# d   e f
# Output:
#   a
#  / \
#  c  b
#  \  / \
#   f e  d

#%%
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

def invert(node):
    if node:
        node.left, node.right = node.right, node.left
        invert(node.left)
        invert(node.right)

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
print("\n")
invert(root)
root.preorder()