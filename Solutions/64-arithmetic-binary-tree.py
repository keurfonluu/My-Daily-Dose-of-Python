#%% [markdown]
# You are given a binary tree representation of an arithmetic expression.
# In this tree, each leaf is an integer value, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
# Write a function that takes this tree and evaluates the expression.
#
# Example
# Input:
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# Output: 45

#%%
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

OP = {
    PLUS: lambda a, b: a + b,
    MINUS: lambda a, b: a - b,
    TIMES: lambda a, b: a * b,
    DIVIDE: lambda a, b: a / b,
}
def evaluate(root):
    return root.val if root.val not in OP.keys() else OP[root.val](evaluate(root.left), evaluate(root.right))

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))