import collections

def uniquePaths(m, n):
    grid = [[0 for i in range(m)] for j in range(n)]
    grid[0][0] = 1
    dirs = [[0, 1], [1, 0]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for x, y in dirs:
                xi, yj = x + i, y + j
                if 0 <= xi < len(grid) and 0 <= yj < len(grid[0]):
                    grid[xi][yj] += grid[i][j]
    return grid[-1][-1]

        # each sq modifies its right and down neighbors



        # grid = [ [0 for i in range(m)] for j in range(n) ]
        # grid[0][0] = 1
        # # right, down
        # dirs = [[0, 1], [1, 0]]
        # q = collections.deque([ [0, 0] ])
        # while len(q) > 0:
        #     curr = q.popleft()
        #     j, i = curr
        #     for x, y in dirs:
        #         xj, yi = x + j, y + i
        #         if 0 <= xj < j and 0 <= yi < i:
        #             grid[xj][yi] = grid[x][j] + 1

print (uniquePaths(3, 2))
# iter over our queue
#  when we pop something off, it looks to the left and above, then
# adds those 2 vals together get its own val
# 
        
        