#%% [markdown]
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example
# ```
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# ```

#%%
class Solution:
    def reverseWords(self, str):
        return " ".join(s[::-1] for s in str.split(" "))

print(Solution().reverseWords("The cat in the hat"))