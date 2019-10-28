def accountsMerge(accounts):
    # find root
    def findroot(i):
        while root[i] != i:
            root[i] = root[root[i]]     # path compression
            i = root[i]
        return i
    
    # union find
    d = {}  # key:val = email:index
    root = list(range(len(accounts)))  
    import pdb; pdb.set_trace() 
    for i, a in enumerate(accounts):
        for email in a[1:]:
            if email in d:
                r1, r2 = findroot(i), findroot(d[email])
                root[r2] = r1
                import pdb; pdb.set_trace()
            else:
                d[email] = i
                
    # merge accounts      
    from collections import defaultdict
    res0 = defaultdict(set)     # key:val = index: {set of emails}
    for i in range(len(accounts)):
        res0[findroot(i)] |= set(accounts[i][1:])
    
    # convert into required format
    res = []
    for k, v in res0.items():    
        res.append([accounts[k][0]] + sorted(v))
    
    return res
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"], ["John", "john00@mail.com", "johan@mail.com"]]
print(accountsMerge(accounts))