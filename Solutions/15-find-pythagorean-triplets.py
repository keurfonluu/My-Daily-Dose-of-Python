#%% [markdown]
# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
#
# Example
# ```
# Input: [3, 5, 12, 5, 13]
# Output: True
# ```

#%%
def findPythagoreanTriplets(nums):
    # Try all possible triplets until one is pythagorean
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if j != i:
                for k, c in enumerate(nums):
                    if k not in { i, j } and a**2 + b**2 == c**2:
                        return True
    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))