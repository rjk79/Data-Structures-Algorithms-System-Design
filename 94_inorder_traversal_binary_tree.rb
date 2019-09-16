def inorder_traversal(root)
    return [] if !root
    left = root.left ? inorder_traversal(root.left) : []
    right = root.right ? inorder_traversal(root.right): []
    return left.concat( [root.val], right )

end