#%% [markdown]
# Given a list of words, group the words that are anagrams of each other.
# (An anagram are words made up of the same letters).
#
# Example
# ```
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
# ```

#%%
def groupAnagramWords(strs):
    n = len(strs)
    mapper = [ 0 ] * n
    count = 0
    for i in range(n):
        if not mapper[i]:
            count += 1
            mapper[i] = count
            tmp = set(list(strs[i]))
            for j, s in enumerate(strs[i+1:]):
                if not mapper[i+j+1]:
                    if set(list(s)) == tmp:
                        mapper[i+j+1] = count
    return [ [ s for s, m in zip(strs, mapper) if m == i+1 ] for i in range(count) ]

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))