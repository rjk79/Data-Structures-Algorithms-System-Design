def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v): #attempt to find a cycle as long as theyre both in graph
                # (make sure they're both connected to any other nodes)
                return u, v
            graph[u].add(v)
            graph[v].add(u)
[[1,2], [1,3], [2,3]]

# graph = {1: [2, 3]
    #      2: [1, ]
    #      3: [1]
# }
# 1 1 2
# 2 3 3