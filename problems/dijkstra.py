
from math import inf 

vertices = int(input("Enter the number of vertices: "))
adjacencyMatrix = []

for i in range(vertices):
    row = [int(i) for i in input().split()]
    adjacencyMatrix.append(row)

start = int(input("Enter the starting node: "))
table = {}

for i in range(vertices):
    allReachableNodes = []
    for index, node in enumerate(adjacencyMatrix[i]):
        if node > 0:
            allReachableNodes.append(index)

    table[i] = allReachableNodes
 

for row in adjacencyMatrix:
    print(" ".join(str(i) for i in row))

for k, v in table.items():
    print(f"{k}: {v}")

def dijkstra(start, end, dist = 0, visited = []):

    if start == end:
        return dist 
    else:
        alldists = [inf]

        for node in table[start]:
            if node not in visited:
                visited.append(node)
                alldists.append(dijkstra(node, end, dist + adjacencyMatrix[start][node], visited))
                visited.remove(node)

    return min(alldists)

dists = []

for i in range(vertices):
    dists.append(dijkstra(start, i))

print("Node Distance from Source")
for i in range(len(dists)):
    print(f"Node {i} -> {dists[i]}")
