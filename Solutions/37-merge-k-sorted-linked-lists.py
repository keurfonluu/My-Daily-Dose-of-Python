#%% [markdown]
# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.

#%%
class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    node_a, node_b = lists
    if node_a.val <= node_b.val:
        node = Node(node_a.val)
        node_a = node_a.next
    else:
        node = Node(node_b.val)
        node_b = node_b.next
    out = node

    while node_a or node_b:
        if node_a and node_b:
            if node_a.val <= node_b.val:
                node.next = Node(node_a.val)
                node_a = node_a.next
            else:
                node.next = Node(node_b.val)
                node_b = node_b.next
            node = node.next
        else:
            node.next = node_a if node_a else node_b
            break
    return out

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))