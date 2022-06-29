#%% [markdown]
# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid.
# The definition of an island is as follows:
# 1. Must be surrounded by water blocks.
# 2. Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally). 
# Assume all edges outside of the grid are water.
#
# Example
# ```
# Input:
#   10001
#   11000
#   10110
#   00000
# Output: 3
# ```

#%%
class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        nx, ny = len(grid[0]), len(grid)
        count, mapper = 0, [ 0 ] * (nx*ny)
        for i in range(ny):
            for j in range(nx):
                if grid[i][j]:
                    idx = i*nx + j
                    if mapper[idx]:
                        island = mapper[idx]
                    else:
                        count += 1
                        island = count
                    mapper[idx] = island
                    
                    # Top
                    idx = (i-1)*nx + j
                    if i > 0 and grid[i-1][j] and not mapper[idx]:
                        mapper[idx] = island

                    # Down
                    idx = (i+1)*nx + j
                    if i < ny-1 and grid[i+1][j] and not mapper[idx]:
                        mapper[idx] = island

                    # Left
                    idx = i*nx + j-1
                    if j > 0 and grid[i][j-1] and not mapper[idx]:
                        mapper[idx] = island

                    # Right
                    idx = i*nx + j+1
                    if j < nx-1 and grid[i][j+1] and not mapper[idx]:
                        mapper[idx] = island
        return mapper

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))

# %%
