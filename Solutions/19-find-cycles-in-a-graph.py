#%% [markdown]
# Given an undirected graph, determine if a cycle exists in the graph.

#%%
def find_cycle(graph):
    for v in graph.values():
        if v == graph:
            return True
    return False

graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print(find_cycle(graph))
graph['c'] = graph
print(find_cycle(graph))
