def minJumps(arr):
    visited = set()
    q = [(len(arr) - 1, 0)]
    while q: #use heap
        curr, currSteps = q.pop() #an index
        if curr == 0: return currSteps
        visited.add(curr)
        neighs = [curr - 1, curr + 1]
        for idx, val in enumerate(arr):
            print(curr)
            if val == arr[curr]: 
                neighs.append(idx)
        neighs = list(filter(lambda a: a not in visited, neighs))
        neighs = list(map(lambda a: (a, currSteps + 1), neighs))
        q.extend(neighs)
    return -1 #cant reach end

print(minJumps([6,1,9]))