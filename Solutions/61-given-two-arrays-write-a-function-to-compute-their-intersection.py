#%% [markdown]
# Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.
# Each element in the result must be unique.
# The result can be in any order.
#
# Example
# ```
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# ```
# Example
# ```
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# ```

#%%
class Solution:
    def intersection(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        n = min(n1, n2)
        tmp1 = sorted(nums1) if n == n1 else sorted(nums2)
        tmp2 = sorted(nums2) if n == n1 else sorted(nums1)

        j = 0
        out = []
        for i in range(n):
            if i == 0 or tmp1[i] != tmp1[i-1]:
                while tmp2[j] < tmp1[i]:
                    j += 1
                if tmp2[j] == tmp1[i]:
                    out.append(tmp1[i])
        return out

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))

# %% [markdown]
# In Python, it could be done simply with ``set(a).intersection(b)``.
# Therefore, try to solve this problem with basic algorithmic functions.