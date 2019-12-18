def serialize(root):
    res = []
    def recurse(root):
        if not root: 
            res.append("#")
            return 
        res.append(str(root.val))
        recurse(root.left)
        recurse(root.right)
    print(res)
    recurse(root)
    return " ".join(res)


def deserialize(data):
    data = iter(data.split(" "))
    
    def recurse():
        currVal = next(data)
        if currVal == "#":
            return None
        curr = TreeNode(int(currVal))
        curr.left = recurse()
        curr.right = recurse()
        return curr
    return recurse()


















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
    #        d   e  f  g
    #      h  i  j k 

    #              1
    #           /     \
    #          2        3
    #         / \      / \
    #        4   5    6   7
    #      8 9  10 11 

a.left = b
a.right = c

b.left = d
b.right = e

d.left = h
d.right = i

c.left = f
c.right = g

e.left = j
e.right = k

print(serialize(a))
print(deserialize(serialize(a)).val)