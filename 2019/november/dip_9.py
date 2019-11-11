#%% [markdown]
# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.
#
# Example
# ```
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
# ```

#%%
def eval(expression):
    # Reduce functions
    reduce = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }

    # Remove white spaces
    expression = expression.replace(" ", "")
    
    # Stacks of integers and operators
    integers, operators = [], []

    # Loop until expression is fully parsed
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isdigit():
            integers.append(int(c))
        elif c in { "+", "-" }:
            operators.append(c)
        elif c == "(":
            operators.append(c)
        elif c == ")":
            # Reduce expression between brackets
            while operators and operators[-1] != "(":
                b = integers.pop()
                a = integers.pop()
                o = operators.pop()
                integers.append(reduce[o](a, b))
            
            # Remove opening bracket from stack
            operators.pop()
        i += 1
    return -1*integers[-1] if operators and operators[-1] == "-" else integers[-1] 

print(eval('- (3 + ( 2 - 1 ) )'))