#%% [markdown]
# Given a list of numbers, where every number shows up twice except for one number, find that one number.
# Challenge: Find a way to do this using O(1) memory.
#
# Example
# ```
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
# ```

#%%
def singleNumber(nums):
    n = len(nums)
    i, idx = 1, 0
    while i < n:
        if i != idx and nums[i] == nums[idx]:
            idx += 1
            i = 0
        else:
            i += 1
    return nums[idx]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))