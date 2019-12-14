#%% [markdown]
# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.
#
# Example
# ```
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
# Output: False

# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"
# Output: True
# ```

#%%
def isSorted(words, order):
    def less_or_equal(word1, word2, order):
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        for c1, c2 in zip(word1[:n], word2[:n]):
            if order[c1] > order[c2]:
                return False
        return n1 <= n2
    
    order = {v: k for k, v in enumerate(order)}
    for i in range(len(words)-1):
        if not less_or_equal(words[i], words[i+1], order):
            return False
    return True

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))