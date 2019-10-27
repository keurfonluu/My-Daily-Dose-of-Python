#%% [markdown]
# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

#%%
class Solution: 
    def longestPalindrome(self, s):
        n = len(s)
        l = set()
        for i in range(n):
            pal, count = "", 0
            for c in s[::-1]:
                if c == s[min(i+count, n-1)]:
                    pal += c
                    count += 1
                else:
                    l.add(pal)
                    pal, count = "", 0
        return max(l, key = len)
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))