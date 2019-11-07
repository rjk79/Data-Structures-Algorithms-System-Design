def findMinHeightTrees(n, edges):
    if n == 1: return [0] 
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in range(n) if len(adj[i]) == 1]

#  has to be more than 2, otherwise we'll collide into your current iter (e.g. 3 and 4 are connected)
    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = adj[i].pop()
            import pdb; pdb.set_trace()
            adj[j].remove(i)
            if len(adj[j]) == 1: newLeaves.append(j)
        leaves = newLeaves
    return leaves

print(findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))