def colorMe(root, n, x):
    # sizes of the .left and .right subtrees
    c = []
    def recurse(root):
        if not root: return 0
        l = recurse(root.left)
        r = recurse(root.right)

        if root.val == x:
            c.append(l)
            c.append(r)
        return l + r + 1

    recurse(root)
    canWin = n // 2 < max(max(c), n - sum(c))
    # print(c)
    return canWin

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)
k = TreeNode(11)

    #             a
    #           /  \
    #          b    c
    #         / \   / \
    #        d   e  f  
    #      h  i  j k 

a.left = b
a.right = c

b.left = d
b.right = e

d.left = h
d.right = i

c.left = f
# c.right = g

e.left = j
e.right = k


print(colorMe(a, 11, 3))
print(colorMe(a, 11, 5))
print(colorMe(a, 11, 2))