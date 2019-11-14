#%% [markdown]
# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.
#
# Example
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

#%%
def word_search(matrix, word):
    # Check rows
    for row in matrix:
        if "".join(row) == word:
            return True

    # Check columns
    for column in zip(*matrix):
        if "".join(column) == word:
            return True
    
    return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))