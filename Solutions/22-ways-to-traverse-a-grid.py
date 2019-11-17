#%% [markdown]
# You have 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.
#
# Example:
# n = 2, m = 2
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.

#%%
def num_ways(n, m):
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    return factorial(n+m-2) / factorial(max(m, n)-1) / factorial(min(m, n)-1)

print(num_ways(2, 2))