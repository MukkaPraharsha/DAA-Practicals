
def floyd_warshal(dist):
    V = len(dist)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist


n = int(input("Enter number of vertices: "))

dist = []

print("Enter adjacency matrix (-1 for no edge):")

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == -1:
            row[j] = float('inf')

    dist.append(row)

result = floyd_warshal(dist)

print("Shortest Distance Matrix:")

for row in result:
    print([int(x) if x != float('inf') else 'INF' for x in row])
