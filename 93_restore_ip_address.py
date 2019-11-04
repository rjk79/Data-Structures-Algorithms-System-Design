def restoreIpAddresses(s):
        
    res = []
    def recurse(curr, idx, count):
        # import pdb; pdb.set_trace()

        if idx == len(s) and count == 4:
            res.append(curr[:-1])
            return
        if count > 4: return
        if idx < len(s):
            recurse(curr + s[idx:idx+1] + ".", idx + 1, count + 1)
        if idx < len(s) - 1 and s[idx] != "0":
            recurse(curr + s[idx:idx+2] + ".", idx + 2, count + 1)
        if idx < len(s) - 2 and s[idx] != "0" and int(s[idx:idx+3]) <= 255:
            recurse(curr + s[idx:idx+3] + ".", idx + 3, count + 1)
    recurse("", 0, 0)
    return res

print (restoreIpAddresses("0000"))
# print (restoreIpAddresses("25525511135"))