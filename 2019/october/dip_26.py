#%% [markdown]
# Given a string, find the length of the longest substring without repeating characters. Can you find a solution in linear time?

#%%
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = 1           # Initial length
        l = set()       # List of characters in current substring
        count = 0       # Counter
        for c in s:
            if c not in l:
                count += 1
                l.add(c)
            else:
                n = max(n, count)
                l = set()
                count = 0
        n = max(n, count)
        return n

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))