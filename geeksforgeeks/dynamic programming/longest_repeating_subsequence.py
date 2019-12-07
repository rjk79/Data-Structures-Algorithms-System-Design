
def recurse(s, curr):
    if not s: return [curr]
    inc = recurse(s[1:], curr + s[0])
    notinc = recurse(s[1:], curr)
    return inc + notinc

print(recurse("AABEBCDD", ""))
