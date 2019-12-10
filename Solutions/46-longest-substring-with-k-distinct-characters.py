#%% [markdown]
# You are given a string ``s``, and an integer ``k``.
# Return the length of the longest substring in ``s`` that contains at most ``k`` distinct characters.
#
# Example
# ```
# Input: aabcdefff, k = 3
# Output: 5
# ```

#%%
def longest_substring_with_k_distinct_characters(s, k):
    n = len(s)      # Length of string
    l = set()       # List of possible substrings with at most k distinct characters 
    for i in range(n-k):
        for j in range(i, n):
            ss = s[i:j+1]
            cond = len(set(list(ss))) > 3
            if cond:
                l.add(ss[:-1])
                break
        if not cond:
            l.add(ss)
    return max(len(ss) for ss in l)

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))