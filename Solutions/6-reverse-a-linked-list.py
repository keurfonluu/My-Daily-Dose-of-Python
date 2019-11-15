#%% [markdown]
# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?
#
# Example
# ```
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
# ```

#%%
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    # Function to print the list
    def printList(self):
        node = self
        output = "" 
        while node:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        node_prev, node_curr, node_next = None, head, None
        while node_curr:
            node_next = node_curr.next  # Save next node
            node_curr.next = node_prev  # Reverse: point current node to previous node
            node_prev = node_curr       # Move previous node to current node
            node_curr = node_next       # Move current node to next node

    # Recursive Solution
    def reverseRecursively(self, head):
        if head.next:
            node = self.reverseRecursively(head.next)
            node.next = head            # Reverse pointer
            head.next = None            # Remove last node
        return head

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()

testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()