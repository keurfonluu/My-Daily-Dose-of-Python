#%% [markdown]
# You are given an sequenceay of integers.
# Return the length of the longest increasing subsequence (not necessarily contiguous) in the sequenceay. 
#
# Example
# ```
# Input: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output: [0, 2, 6, 9, 11, 15]
# ```

#%%
def longest_increasing_subsequence(sequence):
    n = len(sequence)
    lengths = [ 1 ] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lengths[i] = max(lengths[i], lengths[j]+1)
    return max(lengths)

sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(sequence))