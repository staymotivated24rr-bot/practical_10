
def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst = []
    cost = 0

    for w, u, v in sorted(edges):
        a, b = find(u), find(v)

        if a != b:
            parent[a] = b
            mst.append((u, v, w))
            cost += w

            if len(mst) == n - 1:
                break

    return mst, cost


n = 4
edges = [
    (1, 0, 1),
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3)
]

mst, cost = kruskal(n, edges)

if len(mst) == n - 1:
    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("Total Cost:", cost)
else:
    print("Graph is disconnected")
