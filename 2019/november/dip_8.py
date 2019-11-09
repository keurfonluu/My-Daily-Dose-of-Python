#%% [markdown]
# Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

#%%
def distance(s1, s2):
    # Number of insertions/deletions
    count = abs(len(s1) - len(s2))

    # Number of substitutions
    # Count the number of characters in common and in the same order
    icur = 0
    count += len(s1)
    for c1 in s1:
        for i, c2 in enumerate(s2[icur+1:]):
            if c1 == c2:
                icur = i
                count -= 1
                break
    return count
         
print(distance('biting', 'sitting'))