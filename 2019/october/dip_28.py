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
            # Convert string to bracket type
            brackets = {
                "(": "round",   ")": "round",
                "[": "box",     "]": "box",
                "{": "brace",   "}": "brace",
            }

            # +1 if opening new bracket, -1 is closing bracket
            increment = {
                "(": +1,        ")": -1,
                "[": +1,        "]": -1,
                "{": +1,        "}": -1,
            }

            # Brackets are closed before being opened if counter < 0
            counter = { k: 0 for k in set(brackets.values()) }
            for b in s:
                counter[brackets[b]] += increment[b]
                if counter[brackets[b]] < 0:
                    return False

            # Check that opened brackets are all closed i.e. counter == 0
            if all(c == 0 for c in counter.values()):
                return True
            else:
                return False
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