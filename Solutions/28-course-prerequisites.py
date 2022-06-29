#%% [markdown]
# You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key.
# Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.
#
# Example
# ```
# Input: {
#   'CSC300': ['CSC100', 'CSC200'], 
#   'CSC200': ['CSC100'], 
#   'CSC100': []
# }
# Output: ['CSC100', 'CSC200', 'CSC300']
# ```

#%%
def courses_to_take(course_to_prereqs):
    values = [ len(v) for v in course_to_prereqs.values() ]
    courses = [ c for _, c in sorted(zip(values, course_to_prereqs.keys()), reverse = True) ]
    
    prereqs = []
    for course in courses:
        prereqs += course_to_prereqs[course]
    return courses

courses = {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
}
print(courses_to_take(courses))


# %%
