#%% [markdown]
# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:
#
# Each consecutive value describes the prior value.
# ```
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.
# ```
# Your task is, return the nth term of this sequence.

#%%
def sequence(n):
    if n == 1:
        return "1"
    else:
        seq = sequence(n-1)
        out = ""
        count = 1
        for a, b in zip(seq[1:], seq[:-1]):
            if a == b:
                count += 1
            else:
                out += "{}{}".format(count, b)
                count = 1
        out += "{}{}".format(count, seq[-1])
        return out

print(sequence(5))