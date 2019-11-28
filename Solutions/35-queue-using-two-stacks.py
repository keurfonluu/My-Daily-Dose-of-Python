#%% [markdown]
# Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

#%%
class Queue:
    def __init__(self):
        self._values = []
        
    def enqueue(self, val):
        self._values.append(val)

    def dequeue(self):
        return self._values.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())