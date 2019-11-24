#%% [markdown]
# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.
#
# Example
# ```
# grid = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9,  10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
# ]
# ```
# The clockwise spiral traversal of this array is:
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

#%%
def matrix_spiral_print(M):
    # Indice bounds
    imin = 1                # First line is the first to be processed
    imax = len(M)-1
    jmin = 0
    jmax = len(M[0])-1

    # Indices and increments
    i, j = 0, 0             # Current position on the array
    iinc, jinc = 1, 1       # Increments

    # Loop until all the grid has been processed
    count = 0
    spiral = []
    traverse_cols = True
    while count < len(M)*len(M[0]):
        spiral.append(M[i][j])

        # Traverse columns of array
        if traverse_cols:
            cond1 = j == jmax and jinc > 0      # Check if at last column
            cond2 = j == jmin and jinc < 0      # Check if at first column
            if cond1 or cond2:
                # Switch processing direction and increment limits
                jinc *= -1
                if cond1:
                    jmax -= 1
                elif cond2:
                    jmin += 1

                # Go to next row to process
                i += iinc
                traverse_cols = False
            else:
                j += jinc
                
        # Traverse rows of array
        else:
            cond1 = i == imax and iinc > 0      # Check if at last row
            cond2 = i == imin and iinc < 0      # Check if at first row
            if cond1 or cond2:
                # Switch processing direction and increment limits
                iinc *= -1
                if cond1:
                    imax -= 1
                elif cond2:
                    imin += 1

                # Go to next column to process
                j += jinc
                traverse_cols = True
            else:
                i += iinc
        count += 1

    # Print spiral
    print(", ".join(str(x) for x in spiral))

grid = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

matrix_spiral_print(grid)

# %%
