#%% [markdown]
# A unival tree is a tree where all the nodes have the same value.
# Given a binary tree, return the number of unival subtrees in the tree.
#
# Example
# ```
# Input:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# Output: 5
# ```

#%%
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    out = 0
    if root.left and root.right:
        out += count_unival_subtrees(root.left)
        out += count_unival_subtrees(root.right)
        out += int(root.left.val == root.val and root.right.val == root.val)
    elif root.left and not root.right:
        out += count_unival_subtrees(root.left)
        out += int(root.left.val == root.val)
    elif not root.left and root.right:
        out += count_unival_subtrees(root.right)
        out += int(root.right.val == root.val)
    else:
        return 1
    return out

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))