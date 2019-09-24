import collections

def uniquePaths(m, n):
        grid = [ [0 for i in range(m)] for j in range(n) ]
        print grid
        grid[0][0] = 1
        # right, down
        dirs = [[0, 1], [1, 0]]
        q = collections.deque([ [0, 0] ])
        while len(q) > 0:
            curr = q.popLeft()
            j, i = curr
            for x, y in dirs:
                xj, yi = x + j, y + i
                if 0 <= xj < j and 0 <= yi < i:
                    grid[xj][yi] = grid[x][j] + 1

uniquePaths(3, 2)

# iter over our queue
#  when we pop something off, it looks to the left and above, then
# adds those 2 vals together get its own val
# 
        
        