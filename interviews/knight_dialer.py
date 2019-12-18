neighbors = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}
    
def knightDialer(N):
    prev = [1 for _ in range(10)] #moved once
    curr = [0 for _ in range(10)]
    for jump in range(N - 1):
        # look at all neighbors
        # add them to get your own value 
        # (prev val at currCell doesnt matter for its own calculation)
        
        for i in range(len(curr)):
           
            count = 0
            for neighbor in neighbors[i]:
                count += prev[neighbor] 
            curr[i] = count
        prev = curr[::]
        print(curr)
    return sum(prev)
    # returns number of phone numbers

    # N = # of moves
    # N - 1 = # of jumps
    # 1 2 3 
    # 4 5 6
    # 7 8 9
    #   0

    # 2 2 2
    # 3 0 3
    # 2 2 2
    #   2

# print (knightDialer(1))
# print (knightDialer(2))
print (knightDialer(4))
