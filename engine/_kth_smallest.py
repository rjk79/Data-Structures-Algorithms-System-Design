def kthSmallest(root, k):
    allNodes = []
    q = [root]
    while len(q) > 0:
        curr = q.pop()
        allNodes.append(curr)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    allNodes.sort()
    return allNodes[k]
    # use a heap if we're getting new el's often