def numberOfBoomerangs(points):
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            f = p[0]-q[0]
            s = p[1]-q[1]
            cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
        for k in cmap:
            res += cmap[k] * (cmap[k] -1)
        print(cmap)
    return res

print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))