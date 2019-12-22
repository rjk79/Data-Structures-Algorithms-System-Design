# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]               # list of undirected edges
# n  = 5

# n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
def numberOfComponents(n, edges):
    roots = [i for i in range(n)]
    def find(key):
        while key != roots[key]:
            key = roots[key]
        return key
    # import pdb;pdb.set_trace()
    count = n
    for edge in edges:
        root1 = find(edge[0])
        root2 = find(edge[1])
        print(root1, root2)
        if root1 != root2:
            roots[root1] = root2
            count -= 1
        #logic for being in same group
        # else:
        #logic for being in diff group
    # print(roots)
    return count
n = 5 
edges = [[0, 1], [1, 2], [3, 4]]
print(numberOfComponents(n, edges))

# 0 - 1 - 2
# 3 - 4 
