def findInorderSuccessor(root, node):
    # if .PARENT pointer given:
        # if right subtree, find the min val in it
        # if not right subtree, climb up until currNode is parent's .left
    # if not parent pointer: (like a BSearch)
        # if right subtree, same as w/ parent pointer
        # if not right subtree, go down from root
            # if root.val < target.val  #turn right
            #   root = root.right  
            # elif root.val > target.val    #turn left
            #   best = root
            #   root = root.left
            # else: #(root is same as target now)
            #   return best

# \
#  \
#   


# parent pointer
#  \
#  /
# /

# / \ 
#   /
#  /