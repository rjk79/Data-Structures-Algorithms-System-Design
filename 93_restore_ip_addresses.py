def restoreIpAddresses(s):
    res = []
    dfs(s, 0, "", res)
    return res
    
def dfs(s, index, path, res):
    import pdb; pdb.set_trace()

    if index == 4:
        if not s:
            res.append(path[:-1])
        return # backtracking
    for i in xrange(1, 4):
        # the digits we choose should no more than the length of s
        if i <= len(s):
            #choose one digit
            if i == 1: 
                dfs(s[i:], index+1, path+s[:i]+".", res)
            #choose two digits, the first one should not be "0"
            elif i == 2 and s[0] != "0": 
                dfs(s[i:], index+1, path+s[:i]+".", res)
            #choose three digits, the first one should not be "0", and should less than 256
            elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                dfs(s[i:], index+1, path+s[:i]+".", res)

print (restoreIpAddresses("25525511135"))
# s = remaining amt of orig input
# index = group we are working on
# path = what we have
# res is all our paths