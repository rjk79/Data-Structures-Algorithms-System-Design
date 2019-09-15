var buildTree = function (preorder, inorder) {
    if (!preorder.length && !inorder.length) return null

    let root = preorder[0]

    let mid_idx = inorder.indexOf(root)

    let left_inorder = inorder.slice(0, mid_idx)
    let right_inorder = inorder.slice(mid_idx + 1)

    let left_preorder = preorder.filter(el => left_inorder.includes(el))
    let right_preorder = preorder.filter(el => right_inorder.includes(el))

    let rootNode = new TreeNode(root)
    
    rootNode.left = buildTree(left_preorder, left_inorder)
    rootNode.right = buildTree(right_preorder, right_inorder)
    return rootNode
};