import collections
def verticalOrder(root):
        # 5:41
    # [0, 3]
    # [-1, 9] [1, 20]
    # hash with x values
    # vert-higher values will be added first
    if not root: return []
    dic = collections.defaultdict(list)
    q = collections.deque([(0, root)])
    while q:
        val, node = q.popleft()
        dic[val].append(node.val)
        if node.left: q.append((val - 1, node.left))
        if node.right: q.append((val + 1, node.right))
    res = []
    keys = [key for key in dic]
    keys.sort()
    for key in keys:
        res.append(dic[key])
    return res
    # 5:41 - 5:54

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(verticalOrder(a))

# Input: [3,9,20,null,null,15,7]
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# as the tree grows do children get "further" apart? no

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 