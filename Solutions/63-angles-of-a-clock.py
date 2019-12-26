#%% [markdown]
# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

#%%
def calcAngle(h, m):
    angle_hour = (30 * h) % 360
    angle_minute = (6 * m - 0.5 * m) % 360
    return max(angle_hour, angle_minute) - min(angle_hour, angle_minute)

print(calcAngle(3, 30))
print(calcAngle(12, 30))