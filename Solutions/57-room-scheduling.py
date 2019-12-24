#%% [markdown]
# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of times that are required.
#
# Example
# ```
# Input: [(30, 75), (0, 50), (60, 150)]
# Output: 2
# ```

#%%
def number_of_rooms(schedule):
    schedule = sorted(schedule, key = lambda x: x[0])
    times = [ schedule[0] ]
    n_rooms = 1
    for start, end in schedule[1:]:
        times = [ time for time in times if start < time[1] ]
        times.append((start, end))
        n_rooms = max(len(times), n_rooms)
    return n_rooms

print(number_of_rooms([(30, 75), (0, 50), (60, 150)]))