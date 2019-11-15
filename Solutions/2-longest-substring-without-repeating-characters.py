#%% [markdown]
# Given a string, find the length of the longest substring without repeating characters. Can you find a solution in linear time?

#%%
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = 1           # Initial length
        l = set()       # List of characters in current substring
        for c in s:
            if c not in l:
                l.add(c)
            else:
                n = max(n, len(l))
                l = set()
        return max(n, len(l))

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))