def invert_tree(root)
    return nil if !root 
    oldLeft = root.left
    root.left = invert_tree(root.right)
    root.right = invert_tree(oldLeft)
    return root
end