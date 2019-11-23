#%% [markdown]
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Example
# ```
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# ```

#%%
class Solution:
    def moveZeros(self, nums):
        n = len(nums)
        ibeg, icur = 0, 0
        while icur < n:
            if nums[icur]:
                for i in range(icur-ibeg):
                    nums[ibeg+i], nums[icur+i] = nums[icur+i], nums[ibeg+i]
                ibeg += 1
                icur = ibeg
            else:
                icur += 1
        return nums

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)