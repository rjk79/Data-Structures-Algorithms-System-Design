def advantageCount(A, B):
    import pdb; pdb.set_trace()

    sortedA = sorted(A)
    sortedB = sorted(B)
    assigned = {b: [] for b in B}
    remaining = []

    j = 0
    for a in sortedA:
        if a > sortedB[j]:
            assigned[sortedB[j]].append(a)
            j += 1
        else:
            remaining.append(a)
# take the thing at b if there is not just an emptry array
    return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]


# A = [2, 7, 11, 15]
# B = [1, 10, 4, 11]
# sortedA = [2, 7, 11, 15]
# sortedB = [1, 4, 10, 11]

A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
sortedA = [8, 12, 24, 32]
sortedB = [11, 13, 25, 32]

print (advantageCount(A, B))