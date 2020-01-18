# verified
import collections
def validTree(n, edges):
    if not edges: return n == 1
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
                dfs(neigh, node)
            else:
                if parent and neigh != parent: # if youre trying to go back to something thats not your parent
                    valid.append(1)
            
    dfs(0, None)
#       needs to be 1. Acyclic 2. Joint
    return 1 not in valid and len(visited) == n
a = 5
b = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# {0: [1], 1: [0, 2, 3, 4], 2: [1, 3], 3: [2, 1], 4: [1]})
print(validTree(a, b))