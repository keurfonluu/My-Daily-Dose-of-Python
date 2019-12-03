#%% [markdown]
# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
#
# Example 1
# ```
# Input: A = "ab", B = "ba"
# Output: true
# ```
#
# Example 2
# ```
# Input: A = "ab", B = "ab"
# Output: false
# ```
#
# Example 3
# ```
# Input: A = "aa", B = "aa"
# Output: true
# ```
#
# Example 4
# ```
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# ```
#
# Example 5
# ```
# Input: A = "", B = "aa"
# Output: false
# ```

#%%
class Solution:
    def buddyStrings(self, A, B):
        if len(A) == len(B):
            n = len(A)
            if n == 1:
                return False
            elif A == B:
                return A[0] == A[1] if n == 2 else n % 2 == 1
            else:
                count = 0
                for a, b in zip(A, B):
                    count += 1 if a != b else 0
                    if count > 2:
                        return False
                return count == 2
        else:
            return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))