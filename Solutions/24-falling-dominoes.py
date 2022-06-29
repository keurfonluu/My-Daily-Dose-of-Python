#%% [markdown]
# Given a string with the initial condition of dominoes, where:
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
#
# Example
# ```
# Input:  ..R...L..R.
# Output: ..RR.LL..RR
# ```

#%%
class Solution(object):
    def pushDominoes(self, dominoes):
        forward = list(dominoes)
        for i, dominoe in enumerate(dominoes[1:]):
            if forward[i] == "R":
                if dominoe == ".":
                    forward[i+1] = "R"
                elif dominoe == "L":
                    forward[i+1] = "."
        forward = "".join(forward)

        backward = list(dominoes[::-1])
        for i, dominoe in enumerate(dominoes[-2::-1]):
            if backward[i] == "L":
                if dominoe == ".":
                    backward[i+1] = "L"
                elif dominoe == "R":
                    backward[i+1] = "."
        backward = "".join(backward[::-1])

        state = ""
        for fw, bw in zip(forward, backward):
            if fw != bw:
                state += "."
            else:
                state += fw
        return state

print(Solution().pushDominoes('..R...L..R.'))