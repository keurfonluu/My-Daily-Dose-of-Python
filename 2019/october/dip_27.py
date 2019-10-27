#%% [markdown]
# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

#%%
class Solution: 
    def longestPalindrome(self, s):
        n = len(s)      # Length of string
        l = set()       # List of possible subpalindromes
        for i in range(n):
            for j in range(i, n):
                ss = s[i:j]
                if ss == ss[::-1]:
                    l.add(ss)
        return max(l, key = len)
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))