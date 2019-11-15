#%% [markdown]
# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

#%%
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    if root_node:
        # If root value is equal to searched entry, return root value
        if root_node.value == k:
            floor = root_node.value
            ceil = root_node.value
        # If root value is lower than searched entry, recur in right tree
        elif root_node.value < k:
            floor = root_node.value
            floor, ceil = findCeilingFloor(root_node.right, k, floor, ceil)
        # If root value is larger than searched entry, recur in left tree
        elif root_node.value > k:
            ceil = root_node.value
            floor, ceil = findCeilingFloor(root_node.left, k, floor, ceil)
    return floor, ceil

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))