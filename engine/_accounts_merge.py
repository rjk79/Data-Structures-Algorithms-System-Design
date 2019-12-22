def accountsMerge(accounts):
    

# root = [0, 1, 2, 3, 4]
# d = {
#     johnsmith: 0,
#     johnsmith00: 0,
#     johnnybravo: 1,
#     
# }

# 2
# d[johnsmith] = 0

# r1 = 2
# r2 = 0

# root = [2, 1, 2, 3, 4]


def accountsMerge(accounts):
    # find root
    def findroot(i):
        while root[i] != i:
            root[i] = root[root[i]]     # path compression
            i = root[i]
        return i
    # while the value is not = to the idx (not a self loop)
    #  set it to whatever its parent belongs to
    #  now currIdx is the parents idx
    # ex:
    # root[0] != 0
    #   set it to root[2] which is 2
    #   now i = 2 (the new value)
    
    # union find
    d = {}  # key:val = email:index
    root = list(range(len(accounts)))  
    for i, a in enumerate(accounts):
        for email in a[1:]:
            if email in d:
                r1, r2 = findroot(i), findroot(d[email])
                # doesnt compare sizes of sets
                # we are going to make r2 a member of r1
                root[r2] = r1
            else:
                d[email] = i
                
    # merge accounts      
    from collections import defaultdict
    res0 = defaultdict(set)     # key:val ==>> index: {set of emails}
    for i in range(len(accounts)):
        res0[findroot(i)] |= set(accounts[i][1:])
    # convert into required format
    res = []
    for k, v in res0.items():    
        res.append([accounts[k][0]] + sorted(v))
    
    return res
accounts = [["John", "johnsmith", "john00"], ["John", "johnnybravo"], ["John", "johnsmith", "john_newyork"], ["Mary", "mary"], ["John", "john00", "johan"]]
print(accountsMerge(accounts))