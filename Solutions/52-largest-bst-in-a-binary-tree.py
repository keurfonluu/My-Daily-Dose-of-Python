#%% [markdown]
# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

#%%
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

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

def largest_bst_subtree(root):
    pass

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))

#%%
# Use function is_bst from problem 44.