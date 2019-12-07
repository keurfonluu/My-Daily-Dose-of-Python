#%% [markdown]
# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

#%%
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    if root.left and root.right:
        cond = root.left.key <= root.key and root.right.key >= root.key
        condl = is_bst(root.left)
        condr = is_bst(root.right)
        return cond and condl and condr
    elif root.left and not root.right:
        cond = root.left.key <= root.key
        condl = is_bst(root.left)
        return cond and condl
    elif not root.left and root.right:
        cond = root.right.key >= root.key
        condr = is_bst(root.right)
        return cond and condr
    else:
        return True

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))