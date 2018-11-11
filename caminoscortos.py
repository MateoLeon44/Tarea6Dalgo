from collections import deque
import numpy as np
import networkx as nx
input = np.loadtxt('/Users/Santiago/Documents/Dalgo/Tarea6Dalgo/distances5.txt', dtype='i' )
graph = nx.DiGraph()
nodes = input.shape[1]

graph.add_nodes_from([0,nodes-1])


i = 0
j = 0
for row in input:
    np_array = np.array(row)
    i = list(np_array).index(0)
    print(i)
    for column in row:
        if column != -1 and column != 0:
            graph.add_edge(i, j, weight=column)
        if j == nodes-1:
            j = 0
        else:
            j+=1



# Implementación de algoritmo de Dijkstra

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)
    print(nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges(min_node):
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

print("Resultado del algoritmo de dijkstra")    
print(dijkstra(graph, 0))    


  

#Implementación de 

