    #     1
    #    / \
    #   2   3
    #  / \ 
    # 4   5
# nodes oriented as if you turn clockwise
    #     4
    #    / \
    #   5   2
    #      / \ 
    #     3   1

# curr.left.right = curr
# (e.g 2 .right now points to 1)

# curr.left.left = curr.right
# (e.g 2 .left now points to 3)

def upsideDownBinaryTree(root):
    if (not root or not root.left):
        return root
    
    prev = None
    curr = root 
    next = None 
    lastRight = None
    
    while (curr):
        next = curr.left
        
        curr.left = lastRight
        lastRight = curr.right
        
        curr.right = prev
        
        prev = curr
        curr = next

    return prev

#     1
#    / \
#   2   3
#  / \ 
# 4   5
next = 2
lastRight = None
#     1
#    / \
#   2   3
#  / \ 
# 4   5