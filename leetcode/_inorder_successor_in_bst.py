def findInorderSuccessor(root, node):
    # if parent pointer:
        # if right subtree, find the min val in it
        # if not right subtree, climb up until currNode is parent's .left
    # if not parent pointer:
        # if right subtree, same as w/ parent pointer
        # if not right subtree, go down from root
            # if root.val < target.val
            #   root = root.right
            # elif root.val > target.val
            #   best = root
            #   root = root.left
            # else: (root is same as target now)
            #   return best