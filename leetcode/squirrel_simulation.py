Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]

def closestNeighbor():

unvisited = nuts
distances = {}


i, j = squirrel
dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for x, y in dirs:
    xi, yj = x + i, y + j
# run dijkstras 
# calc dist to tree
# calc dist from tree to every nut

# Savings = Nut to Tree - Nut to Squirrel
# min(nut1 to tree - nut1 to squirrel, nut2 to tree - nut2 to squirrel ) 
# + nut2 to tree * 2 
#        T 
# N      
#        N 
#        S 
#        
#        N
