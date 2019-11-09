#%% [markdown]
# You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
# Can you find a solution in O(n) time?

#%%
def staircase(n):
    # Just Fibonacci
    if n:
        if n in { 1, 2 }:
            return n
        else:
            return staircase(n-1) + staircase(n-2)
  
print(staircase(4))
print(staircase(5))