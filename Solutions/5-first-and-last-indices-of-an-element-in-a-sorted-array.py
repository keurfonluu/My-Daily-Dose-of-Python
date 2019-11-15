#%% [markdown]
# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.
#
# Example
# ```
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]
# ```

#%%
class Solution: 
    def getRange(self, arr, target):
        # Find first occurence
        first = None
        for i, x in enumerate(arr):
            if x == target:
                first = i
                break

        # Return [ -1, -1 ] if first occurence not found
        if first is None:
            return [ -1, -1 ]

        # Find last occurence
        last = first
        for x in arr[i+1:]:
            if x != target:
                break
            else:
                last += 1
        last = -1 if last == first else last
        return [ first, last ]
            
# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))