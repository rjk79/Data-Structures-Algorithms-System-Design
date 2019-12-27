import collections
def calcEquation(equations, values, queries):
#         graph
    graph = collections.defaultdict(dict)
    for idx, equation in enumerate(equations):
        graph[equation[0]][equation[1]] = values[idx]
        graph[equation[1]][equation[0]] = 1/values[idx]
    res = []
    def dfs(currVar, target, visited):
        if currVar == target: 
            return 1
        canVisit = False
        visited.add(currVar)
        for neigh in graph[currVar]:
            if neigh not in visited:
                canVisit = True
                return graph[currVar][neigh] * dfs(neigh, target, visited)
        if not canVisit: return 0
    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            res.append(-1.0)
        else:
            ans = dfs(query[0], query[1], set())
            if ans:
                res.append(ans)
            else:
                res.append(-1.0)
    return res         
# a / c

a = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
b = [3.0,4.0,5.0,6.0]
c = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print(calcEquation(a, b, c))
