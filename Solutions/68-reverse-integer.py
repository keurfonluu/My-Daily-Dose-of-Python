#%% [markdown]
# Write a function that reverses the digits a 32-bit signed integer, x.
# Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1].
# The function returns 0 when the reversed integer overflows.
#
# Example
# ```
# Input: 123
# Output: 321
# ```

#%%
class Solution:
    def reverse(self, x):
        out = int("".join(i for i in str(x)[::-1]))
        return out if -2**31 <= out <= 2**31-1 else 0

print(Solution().reverse(123))
print(Solution().reverse(2**31))