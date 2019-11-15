#%% [markdown]
# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
# Try to do it in a single pass of the list.
#
# Example
# ```
# Given [4, 7, 1 , -3, 2] and k = 5, 
# return true since 4 + 1 = 5.
# ```

#%%
def two_sum(l, k):
    s = set(l)              # No space complexity constraint
    for x in l:
        if -(x-k) in s:     # Searching a value in a set is O(1)
            return True
    return False

print(two_sum([4,7,1,-3,2], 5))