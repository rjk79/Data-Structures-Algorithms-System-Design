def intervalIntersection(a, b):
    i,j, res = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i].end < b[j].start:
            i += 1
        elif b[j].end < a[i].start:
            j += 1
        else:
            res.append(Interval(max(a[i].start, b[j].start), min(a[i].end, b[j].end))) 
            if a[i].end > b[j].end:
                j += 1
            else:
                i += 1
    return res
print(intervalIntersection([[1, 2]], [[4, 3]]))