import numpy as np
import networkx as nx
input = np.loadtxt("distances5.txt", dtype='i' )
graph = nx.Graph()
nodes = input.shape[1]

graph.add_nodes_from([0,nodes-1])


i = 0
j = 0
for row in input:
    np_array = np.array(row)
    i = list(np_array).index(0)
    print(i)
    for column in row:
        if column != 1 & column != 0:
            graph.add_edge(i, j, weight=column)
        if j == nodes-1:
            j = 0
        else:
            j+=1

print(graph.edges)
