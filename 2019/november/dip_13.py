#%% [markdown]
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum â‰¥ s. If there isn't one, return 0 instead.
#
# Example
# ```
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# ```
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

#%%
class Solution:
    def minSubArrayLen(self, nums, s):
        n = len(nums)+1         # Initial length
        for i in range(len(nums)):
            val, count = 0, 0
            for x in nums[i:]:
                val += x
                count += 1
                if val >= s:
                    if val == s and count < n:
                        n = count
                    break
        return n if n <= len(nums) else 0

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))