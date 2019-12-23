#%% [markdown]
# You are given a string of parenthesis.
# Return the minimum number of parenthesis that would need to be removed in order to make the string valid.
# "Valid" means that each open parenthesis has a matching closed parenthesis.
#
# Example
# ```
# Input: "()())()"
# Output: 1
# ```

#%%
def count_invalid_parenthesis(string):
    stack = []
    for p in string:
        if p == "(":
            stack.append(p)
        else:
            if stack and stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append(p)
    return len(stack)

print(count_invalid_parenthesis("()())()"))

#%% [markdown]
# This is basically the same as problem 4.