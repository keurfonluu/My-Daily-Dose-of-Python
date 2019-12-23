#%% [markdown]
# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.
#
# Example
# ```
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# ```

#%%
def findRanges(nums):
    out = []
    i1, i2 = 0, 0
    while i2 < len(nums)-1:
        if nums[i2+1] in {nums[i2], nums[i2]+1}:
            i2 += 1
        else:
            out.append("{}->{}".format(nums[i1], nums[i2]))
            i2 += 1
            i1 = i2
    out.append("{}->{}".format(nums[i1], nums[i2]))
    return out

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))