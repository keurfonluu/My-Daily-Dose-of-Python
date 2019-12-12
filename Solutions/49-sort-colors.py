#%% [markdown]
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Can you do this in a single pass?
#
# Example
# ```
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# ```

#%%
class Solution:
    def sortColors(self, nums):
        i, imin, imax = 0, 0, len(nums)-1
        while i <= imax:
            # Move 0 to position imin
            if nums[i] == 0:
                nums[i], nums[imin] = nums[imin], nums[i]
                imin += 1
                i += 1
            # 1 is always in the middle
            elif nums[i] == 1:
                i += 1
            # Move 2 to position imax
            elif nums[i] == 2:
                nums[i], nums[imax] = nums[imax], nums[i]
                imax -= 1
        return nums

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)

Solution().sortColors(nums)
print("After Sort: ")
print(nums)

#%% [markdown]
# This is exactly the same as problem 7.