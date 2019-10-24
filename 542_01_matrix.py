def updateMatrix(matrix):
        res = [ [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def bfs(point):
            visited = [ [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
            count = 0   
            q = [point]
            while q:
                newQ = []
                for node in q:
                    i, j = node
                    visited[i][j] = 1
                    if matrix[i][j] == 0: return count
                    for x, y in dirs:
                        xi, yj = x+i, y+j
                        if 0 <= xi < len(matrix) and 0 <= yj < len(matrix[0]) and visited[xi][yj] == 0:
                            newQ.append([xi, yj])
                            
                q = newQ
                count += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    res[i][j] = bfs([i, j])
        return res
print (updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print (updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))