
import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    cost = 0

    while pq:
        w, v = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True
        cost += w

        for neigh, edge in graph[v]:
            if not visited[neigh]:
                heapq.heappush(pq, (edge, neigh))

    return cost


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter source, destination and weight:")

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print("Minimum Spanning Tree Cost:", prim(graph))
