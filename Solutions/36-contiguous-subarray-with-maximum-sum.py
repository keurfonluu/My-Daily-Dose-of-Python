#%% [markdown]
# You are given an array of integers.
# Find the maximum sum of all possible contiguous subarrays of the array.
#
# Example
# ```
# Input: [34, -50, 42, 14, -5, 86]
# Output: [42, 14, -5, 86]
# ```

#%%
def max_subarray_sum(arr):
    n = len(arr)    # Length of array
    l = []          # List of possible contiguous subarrays
    for i in range(n):
        for j in range(i, n):
            l.append(arr[i:j+1])
    return max(l, key = lambda x: sum(x))

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))