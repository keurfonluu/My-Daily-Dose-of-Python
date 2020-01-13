#%% [markdown]
# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than ``2 * (n - 1)`` comparisons.

#%%
def find_min_max(nums):
    # Initialize min and max
    if nums[0] <= nums[1]:
        minval = nums[0]
        maxval = nums[1]
    else:
        minval = nums[1]
        maxval = nums[0]

    # Update min and max
    for val in nums[2:]:
        if val < minval:
            minval = val
        elif val > maxval:
            maxval = val
    return (minval, maxval)
    
print(find_min_max([3, 5, 1, 2, 4, 8]))