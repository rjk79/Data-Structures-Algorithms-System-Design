import collections
def validTree(n, edges):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited = set()
    valid = []
    def dfs(node, parent):
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                import pdb;pdb.set_trace()
                dfs(neigh, node)
            else:
                if node == 3: import pdb;pdb.set_trace()

                if parent and neigh != parent:
                    valid.append(1)
            
    dfs(0, None)
    return 1 not in valid and len(visited) == len(graph)

a = 5
b = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# {0: [1], 1: [0, 2, 3, 4], 2: [1, 3], 3: [2, 1], 4: [1]})
print(validTree(a, b))