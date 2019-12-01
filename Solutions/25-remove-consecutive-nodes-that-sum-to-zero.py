#%% [markdown]
# Given a linked list of integers, remove all consecutive nodes that sum up to 0.
#
# Example
# ```
# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10
# ```

#%%
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def removeConsecutiveSumTo0(node):
    def check_node(node):
        """
        Return number of nodes to remove from given node.
        """
        n_node = 0          # Number of nodes to remove
        node_sum = 0        # Sum of node values
        node_cur = node
        while node_cur:
            node_sum += node_cur.value
            n_node += 1
            node_cur = node_cur.next
            if node_sum == 0:
                return n_node
        return 0
    
    # First node
    while True:
        n_node = check_node(node)
        if n_node:
            for _ in range(n_node):
                node = node.next
        else:
            break

    # Remove consecutive nodes that sum to zero
    node_cur = node.next
    node.next = None
    out = node
    while node_cur:
        n_node = check_node(node_cur)
        if n_node:
            for _ in range(n_node-1):
                node_cur = node_cur.next
        else:
            node.next = node_cur
            node = node.next
        node_cur = node_cur.next
    return out

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value)
    node = node.next