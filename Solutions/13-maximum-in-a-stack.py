#%% [markdown]
# Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty).
# Each method should run in constant time.

#%%
class MaxStack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if len(self.data):
            return self.data.pop()

    def max(self):
        if len(self.data):
            return max(self.data)
        else:
            return None

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
s.pop()
s.pop()
print(s.max())