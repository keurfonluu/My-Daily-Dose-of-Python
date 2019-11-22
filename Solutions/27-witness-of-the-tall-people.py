#%% [markdown]
# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?
#
# Example
# ```
# Input: [3, 6, 3, 4, 1]  
# Output: 3
# ```

#%%
def witnesses(heights):
    n = 1               # First in line can always see in front of him
    h = heights[-1]     # Height of person in front of current person
    for height in heights[-2::-1]:
        n += 1 if height > h else 0
        h = max(height, h)
    return n

print(witnesses([3, 6, 3, 4, 1]))