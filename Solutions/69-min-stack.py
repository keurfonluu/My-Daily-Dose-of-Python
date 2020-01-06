#%% [markdown]
# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Note: be sure that pop() and top() handle being called on an empty stack.

#%%
class minStack(object):
    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        return self.values.pop(-1) if self.values else None

    def top(self):
        return self.values[-1] if self.values else None

    def getMin(self):
        return min(self.values) if self.values else None

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
x.pop()
print(x.top())
print(x.getMin())