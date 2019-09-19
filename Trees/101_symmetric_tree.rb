def is_symmetric(root)
    symmetric(root, root)
end

def symmetric(node1, node2)
    return true if !node1 && !node2
    return false if (!node1 && node2) || (node1 && !node2)
    return node1.val == node2.val && symmetric(node1.right, node2.left) && symmetric(node1.left, node2.right)
    # node1.right and node2.left are the inner pair
    # node1.left and node2.right are outer pair
    # they will stay paired
    # if there was a row with 5s and 6s then there would be an inner pair
    # more outer pair
    # and most outer
end

# [1,2,2,3,4,4,3]
# 1   T && 2right 2left   2left 2right
#     T  3right   3left   4right 4left   

        #     1
        #    / \
        #   2   2
        #  / \ / \
        # 3  4 4  3
    