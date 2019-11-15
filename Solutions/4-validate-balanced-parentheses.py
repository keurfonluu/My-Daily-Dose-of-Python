#%% [markdown]
# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example
# ```
# Input: "((()))"
# Output: True

# Input: "[()]{}"
# Output: True

# Input: "({[)]"
# Output: False
# ```

#%%
class Solution:
    def isValid(self, s):
        if s:
            # Corresponding opening brackets
            brackets = { ")": "(", "]": "[", "}": "{" }

            # Check that brackets are closed in the correct order
            stack = []
            for b in s:
                if b in { "(", "[", "{" }:
                    stack.append(b)
                else:
                    if stack:
                        if stack[-1] == brackets[b]:
                            stack.pop(-1)
                        else:
                            return False
                    # Not valid if closing bracket while stack is empty
                    else:
                        return False

            # Not all brackets are closed if stack is not empty
            if stack:
                return False
            else:
                return True
        # True if empty string
        else:
            return True

# Test Program
s = "()(){(())"
print(Solution().isValid(s))

s = ""
print(Solution().isValid(s))

s = "([{}])()"
print(Solution().isValid(s))