#%% [markdown]
# Given a sorted list of numbers, change it into a balanced binary search tree.
# You can assume there will be no duplicate numbers in the list.

#%%
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalancedBST(nums):
    n = len(nums)
    if n == 1:
        node = Node(nums[0])
    else:
        mid = n // 2
        left = createBalancedBST(nums[:mid])
        right = createBalancedBST(nums[mid+1:])
        node = Node(nums[mid], left, right)
    return node

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))