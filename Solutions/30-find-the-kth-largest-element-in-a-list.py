#%% [markdown]
# Given a list, find the k-th largest element in the list. 
#
# Example
# ```
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# ```

#%%
def findKthLargest(nums, k):
    # Partial selection sort
    for i in range(k):
        for j, x in enumerate(nums[i+1:]):
            if x >= nums[i]:
                nums[i], nums[i+1+j] = nums[i+1+j], nums[i]
    return nums[k-1]

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))