
def numIslands(grid):
            #     stack?
    #     put all the water tiles into a stack and then pick off the top 
    #     adding in all neighbors that are not water
    #     whenever you hit a land, make it water, count ++, set flag to true
    #     when its not a land set flag to false
    stack = []
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    traversingLand = False
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                stack.append([i, j])
                
    while len(stack) > 0:
        curr = stack.pop()
        i, j = curr
        if grid[i][j] == "1":
            grid[i][j] = "0"
            if not traversingLand: 
                traversingLand = True
                count += 1
        else:
            traversingLand = False
            
        for x, y in dirs:
            xi, yj = x + i, y + j
            
            if 0 <= xi < len(grid) and 0 <= yj < len(grid[0]):
                if grid[xi][yj] == "1":
                    stack.append([xi, yj])

    return count

print (numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print (numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 1