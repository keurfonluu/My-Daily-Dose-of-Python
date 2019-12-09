#%% [markdown]
# Given a binary tree, return all values given a certain height ``h```.
#
# Example
# ```
# Input:
#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
# Output: [4, 5, 7]
# ```

#%%
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, depth, height):
    if depth == height:
        out = [ root.value ]
    else:
        out = []
        out += valuesAtHeight(root.left, depth+1, height) if root.left else []
        out += valuesAtHeight(root.right, depth+1, height) if root.right else []
    return out

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 1, 3))