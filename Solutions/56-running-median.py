#%% [markdown]
# You are given a stream of numbers.
# Compute the median for each new element.
#
# Example
# ```
# Input: [2, 1, 4, 7, 2, 0, 5]
# Output: [2, 1.5, 2, 3, 2, 2, 2]
# ```

#%%
def running_median(stream):
    # Median of a sorted array
    def median(x):
        imid = len(x) // 2
        if len(x) % 2 == 0:
            return 0.5 * (x[imid-1] + x[imid])
        else:
            return x[imid]

    # Insertion sort algorithm
    n = len(stream)
    i = 1
    out = [ stream[0] ]
    while i < n:
        x = stream[i]
        j = i - 1
        while j >= 0 and stream[j] > x:
            stream[j+1] = stream[j]
            j -= 1
        stream[j+1] = x
        i += 1
        out.append(median(stream[:i]))
    return out

print(running_median([2, 1, 4, 7, 2, 0, 5]))