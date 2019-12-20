import collections
class Solution:
    def criticalConnections(self, n, connections):
            
        graph = collections.defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
            
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
        
        cur = 0
        start = 0
        res = []
        self.cur = 0
        
        def dfs(node,parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur+=1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n,node)
                    
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l
                
        dfs(0,None)
        print(low)
        for v in connections:
            if low[v[0]]>dfn[v[1]] or low[v[1]]>dfn[v[0]]:
        
                res.append(v)
        return res
soln = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(soln.criticalConnections(n, connections))
