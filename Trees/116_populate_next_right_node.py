def populateNextRightNode(root):
    q = [root]
    while len(q) > 0:
        i = 0
        while i < len(q) - 1:
            # last one's "next" should be set to None (already done)
            q[i].next = q[i + 1]
            i += 1

        newQ = []
        for node in q:
            if node.left: newQ.append(node.left)
            if node.right: newQ.append(node.right)
        q = newQ
    return root







\
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
a = Node(1, None, None, None)
b = Node(2, None, None, None)
c = Node(3, None, None, None)
d = Node(4, None, None, None)
e = Node(5, None, None, None)
f = Node(6, None, None, None)
g = Node(7, None, None, None)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

populateNextRightNode(a)

# def inorder_traversal(root):
#     if not root: return [] 
#     left = root.left if inorder_traversal(root.left) else []
#     right = root.right if inorder_traversal(root.right) else []
#     return left + [root.val] + right 

# inorder_traversal(a)

# dfs
#       a
#     /  \
#    b     c
#  /  \   /  \
# d    e f    g