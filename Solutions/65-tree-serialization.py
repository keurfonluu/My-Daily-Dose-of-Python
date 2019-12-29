#%% [markdown]
# You are given the root of a binary tree. You need to implement 2 functions:
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
# For this problem, often you will be asked to design your own serialization format.
# However, for simplicity, let's use the pre-order traversal of the tree. 

#%%
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

def serialize(root):
    if not root:
        return "# "
    else:
        out = "{} ".format(root.val)
        out += serialize(root.left)
        out += serialize(root.right)
        return out

def deserialize(data):
    if not data:
        return
    else:
        val = data.pop(0)
        if val == " ":
            pass
        if val == "#":
            return None
        else:
            root = Node(int(val))
            root.left = deserialize(data)
            root.right = deserialize(data)
        return root

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'.split(" ")))

# %% [markdown]
# For ``deserialize``, we use a list instead of a string as strings are immutable.