#%% [markdown]
# You are given an array of integers.
# Return the largest product that can be made by multiplying any 3 integers in the array.
#
# Example
# ```
# Input: [-4, -4, 2, 8]
# Output: 128
# ```

#%%
def maximum_product_of_three(lst):
    maxprod = lst[0] * lst[1] * lst[2]
    for i, x1 in enumerate(lst[:-2]):
        for j, x2 in enumerate(lst[i+1:-1]):
            for x3 in lst[i+j+2:]:
                maxprod = max(x1*x2*x3, maxprod)
    return maxprod

print(maximum_product_of_three([-4, -4, 2, 8]))