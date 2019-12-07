wines = [1, 4, 2, 3]
N = 4
def recurse(wines):
    if not wines: return 0
    print(wines)
    year = N - len(wines) + 1
    return max(year * wines[0] + recurse(wines[1:]), year * wines[-1] + recurse(wines[:-1]))
print(recurse(wines))
