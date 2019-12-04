# The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7

# while the diagrams for the outputs are:

#           4
#         /   \
#       3      6      and    2
#             / \           /
#            5   7         1

# Solution:
# at target we only want to pass up self (root of new subtree) and R
# at target's parent we want to pass up self (old subtree) and L (new subtree)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(5)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

def splitBST(root, V):
    res = [None, None]
    if not root: return res
    if root.val <= V:
        res[0] = root
        rightRes = splitBST(root.right, V)
        root.right = rightRes[0]
        res[1] = rightRes[1]
    else:
        res[1] = root
        leftRes = splitBST(root.left, V)
        root.left = leftRes[1]
        res[0] = leftRes[0]
    return res


def preorder(root):
    print(root.val)
    if root.left: preorder(root.left)
    if root.right: preorder(root.right)


answer = splitBST(a, 2)
preorder(answer[0])
print("---------")
preorder(answer[1])

# if we need to go up further to right, [1] will be updated
#                             to left, [0] will be updated but .right will hold old [0]
# so you'd get:
#    4         0
#   / \         \
#  3   6         2
#     / \       /
#    5   7     1

# every node passes itself up and child
4
res = [2, 4] ->
leftRes = [2, 3]
  4
 /
3
# passes itself up via [1]
# passes child up via [0]

2
res = [2, 3]   
rightRes = [None, 3] 
# OPPOSITE passing:
# child, 3, passes thru via [1]
# passes itself up via [0]
                
2
 \
None


3
res = [None, 3] 
# passes itself up via [1]
# left child, None, passes thru via [0]
# if 3 had a .left like 2.5 it still wouldnt be passed via res
# b/c it'd ret [None, 2.5] and this curr call only reads [0]
leftRes = [None, None] 
root.left = None
   3
  /
None
