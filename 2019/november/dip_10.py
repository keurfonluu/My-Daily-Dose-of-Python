#%% [markdown]
# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.
#
# Example
# ```
# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: [3, 1, 3, 1]
# ```

#%%
def findSequence(seq):
    n = 0       # Initial length of longest subset
    idx = 0     # Initial index of start of longest subset
    for i, x in enumerate(seq[:-1]):
        # Make subset
        l = [ x ]
        for val in seq[i+1:]:
            l.append(val)

            # Break loop if subset has more than 2 unique numbers
            if len(set(l)) > 2:
                break

        # Update longest subset
        nl = len(l) - 1
        if nl > n:
            n = nl
            idx = i
    return seq[idx:idx+n]

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))