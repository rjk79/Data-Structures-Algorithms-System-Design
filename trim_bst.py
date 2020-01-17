def trimmer(root, L, R):
    if not root:
        return None
    elif root.val > R:
        trimmer(root.left, L, R)
    elif root.val < L:
        trimmer(root.right, L, R)
    else:
        root.left = trimmer(root.left, L, R)
        root.right = trimmer(root.right, L, R)
        return root
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

b.left = c
b.right = d

#   b
#  / \
# c   d

#   2
#  / \
# 3   4

# l, self, r
# l self 
# self r
# l
# r
# find idx of 
answer = trimmer(b)

q = [answer]
while q:
    print(q)
    newQ = []
    for node in q:
        if node.left: newQ.append(node.left)
        if node.right: newQ.append(node.right)
    q = newQ
# 1, 2
#     1
#    / \
#   0   2


# root = 1
# .left = None
# .right = 2
# 
# root = 0
# => None (root.right)

# root = 2
# .left = None
# .right = None
# =>2

# 1, 3
#     3
#    / \
#   0   4
#   \
#    2
#    /
#    1

# root = 3
# .left = 
# .right =
# 
# root = 0
# => 
# 
# root = 2
# .left = None
# .right = 1
# => 2

# root = 1
# => 1 
