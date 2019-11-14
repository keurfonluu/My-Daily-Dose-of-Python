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
    def is_present(word, lst):
        """
        Check if word is present in string (list of characters).
        """
        n, m = len(word), len(lst)
        for i in range(m-n+1):
            if "".join(lst[i:i+n]) == word:
                return True
        return False

    # Check rows
    for row in matrix:
        if is_present(word, row):
            return True

    # Check columns
    for column in zip(*matrix):
        if is_present(word, column):
            return True
    
    return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))