#%% [markdown]
# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
#
# Example
# ```
# Input:
#     a
#    / \
#   b   c
#  /
# d
# Output: (d, 3)
# ```

# %%
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val

def deepest(node, depth):
    if node.left and node.right:
        vl, dl = deepest(node.left, depth+1)
        vr, dr = deepest(node.right, depth+1)
        return (vl, dl) if dl >= dr else (vr, dr)
    elif node.left and not node.right:
        return deepest(node.left, depth+1)
    elif not node.left and node.right:
        return deepest(node.right, depth+1)
    else:
        return (node.val, depth)        

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root, 1))