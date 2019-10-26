#%% [markdown]
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Example
# ```
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# ```

#%%
# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __len__(self):
        """
        Number of nodes until last node in list.
        """
        n = 1
        node = self.next
        while node:
            n += 1
            node = node.next
        return n

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Initialize output list
        val = l1.val + l2.val
        out = ListNode(val % 10)
        inc = 0 if val < 10 else 1

        # Current node positions
        node1, node2 = l1, l2
        node = out

        # Sum common digits
        n1, n2 = len(l1), len(l2)
        n = min(n1, n2)
        for _ in range(n-1):
            node1, node2 = node1.next, node2.next
            val = node1.val + node2.val + inc
            node.next = ListNode(val % 10)
            node = node.next
            inc = 0 if val < 10 else 1

        # Append extra digits
        if n1 != n2:
            m = max(n1, n2)
            node1 = node1 if m == n1 else node2
            for _ in range(m-n):
                node1 = node1.next + inc
                node.next = ListNode(node1.val)
                node = node.next
                inc = 0
        else:
            # Handle case if last sum was higher than 9
            if val > 9:
                node.next = ListNode(1)
        return out

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next

# %%