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
        self.minval = []

    def push(self, x):
        self.values.append(x)
        if not self.minval or x <= self.getMin():
            self.minval.append(x)

    def pop(self):
        if not self.values:
            return None
        else:
            x = self.values.pop(-1)
            if x == self.getMin():
                self.minval.pop(-1) 
            return x

    def top(self):
        return self.values[-1] if self.values else None

    def getMin(self):
        return self.minval[-1] if self.minval else None

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
x.pop()
print(x.top())
print(x.getMin())