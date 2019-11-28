#%% [markdown]
# You are given an array of intervals - that is, an array of tuples (start, end).
# The array may not be sorted, and could contain overlapping intervals.
# Return another array where the overlapping intervals are merged.
#
# Example
# ```
# Input: [(1, 3), (5, 8), (4, 10), (20, 25)]
# Output: [(1, 3), (4, 10), (20, 25)]
# ```

# %%
def merge(intervals):
    out = []
    processed = set()
    for i, (a, b) in enumerate(intervals):
        if i not in processed:
            for j, (c, d) in enumerate(intervals[i+1:]):
                if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
                    a = min(a, c)
                    b = max(b, d)
                    processed.add(i+j+1)
            out.append((a, b))
    return out

print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))