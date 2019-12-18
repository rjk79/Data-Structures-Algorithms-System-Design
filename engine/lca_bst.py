def lowestCommonAncestor(root, p, q):
    #       look right
    # import pdb;pdb.set_trace()
    if root.val < p.val and root.val < q.val:
        lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        lowestCommonAncestor(root.left, p, q)
    else:
        return root.val


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = TreeNode(0)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
# 0 2 3 4 5 6 7 8 9 
# [6,2,8,0,4,7,9,null,null,3,5]
#        6
#     2     8
#   0   4  7  9
#      3 5

f.left = b
f.right = h
b.left = a
b.right = d
h.left = g
h.right = i
d.left = c
d.right = e
# 6, 2, 4
print(lowestCommonAncestor(f, b, d))
print(lowestCommonAncestor(f, b, h))