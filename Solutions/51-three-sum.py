#%% [markdown]
# Given an array, ``nums``, of n integers, find all unique triplets (three numbers, a, b, & c) in ``nums`` such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero in ``nums``, and that the triplets must not be duplicates.
#
# Example
# ```
# Input: [0, -1, 2, -3, 1]
# Ouput: [0, -1, 1], [2, -3, 1]
# ```

#%%
class Solution(object):
    def threeSum(self, nums):
        out = set()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if j != i:
                    for c in nums:
                        if a + b + c == 0:
                            out.add(tuple(sorted([a, b, c])))
        return out

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))