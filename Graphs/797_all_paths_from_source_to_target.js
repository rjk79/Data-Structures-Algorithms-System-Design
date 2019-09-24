var allPathsSourceTarget = function (graph) {
    let target = graph.length - 1

    const _allPaths = function (node) {
        debugger
        if (node == target) return [target]
        let res = []
        graph[node].forEach(neighbor => {
            // returns a 2d arr. so iter over it. 
            // to each thing, add in the current node
            _allPaths(neighbor).forEach(path => {
                // push each 2d arr to the main array
                res.push([node].concat(path))
            })
        })
        return res
    }
    return _allPaths(0)
};
console.log(allPathsSourceTarget([[1, 2], [3], [3], []]))

// res = [[0, 1, 3], [0, 2, 3]]
// res = [[3]]

// def allPathsSourceTarget(self, graph):
//     N = len(graph)

//     def solve(node):
//     if node == N - 1: return [[N - 1]]
//     ans = []
//     for nei in graph[node]:
//         for path in solve(nei):
//             ans.append([node] + path)
//     return ans

//     return solve(0)

