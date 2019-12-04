def is_valid_bst(root, lowerLim = -Float::INFINITY, upperLim = Float::INFINITY)
    return true if !root  
    isValid = lowerLim < root.val && upperLim > root.val
    # pass down the value of each root to create upper and lower limits 
    return isValid && is_valid_bst(root.left, lowerLim, root.val) && is_valid_bst(root.right, root.val, upperLim)
end

        #      10
        #     /  \  
        #    5    15
        #   / \   / \
        #     11 6   20 