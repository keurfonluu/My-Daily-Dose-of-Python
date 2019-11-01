#%% [markdown]
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: Try sorting the list using constant space.
#
# Example
# ```
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
# ```

#%%
def sortNums(nums):
    i, imin, imax = 0, 0, len(nums)-1
    while i < imax:
        # Move 1 to position imin
        if nums[i] == 1:
            nums[i], nums[imin] = nums[imin], nums[i]
            imin += 1
            i += 1
        # 2 is always in the middle
        elif nums[i] == 2:
            i += 1
        # Move 3 to position imax
        elif nums[i] == 3:
            nums[i], nums[imax] = nums[imax], nums[i]
            imax -= 1
    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))