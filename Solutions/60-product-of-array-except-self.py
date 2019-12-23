#%% [markdown]
# You are given an array of integers.
# Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.
# You cannot use division in this problem.
#
# Example
# ```
# Input: [1, 2, 3, 4, 5]
# Output: [120, 60, 40, 30, 24]
# ```

#%%
def products(nums):
    out = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        out.append(prod)
    return out

print(products([1, 2, 3, 4, 5]))