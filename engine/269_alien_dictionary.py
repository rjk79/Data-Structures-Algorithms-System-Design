import collections
def alienOrder(words):
#       key is beaten by: (values)
    prereqs = collections.defaultdict(list)
    for pair in zip(words[:-1], words[1:]):
        differIdx = 0
        while differIdx < min(len(pair[0]), len(pair[1])) and pair[0][differIdx] == pair[1][differIdx]:
            differIdx += 1
        # import pdb;pdb.set_trace()
        print(pair[1][differIdx])
        if pair[1][differIdx] in prereqs[pair[0][differIdx]]: 
            return ""
        prereqs[pair[1][differIdx]].append(pair[0][differIdx])
        
    firstChar = None
    for char in list("".join(words)):
        if char not in prereqs: firstChar = char 
    
    res = [firstChar]
    q = collections.deque([firstChar])
    visited = set()
    while q:
        char = q.popleft()
        visited.add(char)
        for key in prereqs:
            if char in prereqs[key]: prereqs[key].remove(char)
            if not prereqs[key] and key not in visited: 
                q.append(key)
                res.append(key)
    if res: return "".join(res)
        

print(alienOrder(["wrt","wrf","er","ett","rftt"]))
# print(alienOrder(["wrt","wrf","er","ett","rftt"]))


# if we didn't remove all prereqs then dont add it into queue, charsToProcess
# (we dont have enough info to place it. there are more chars that come before it)
# if we dont add something to Q on this iter, then either the next succ for the current letter will add something OR
# the next letter's successors will be added 