    def dfs(node: TreeNode, parent: TreeNode, grandParent: TreeNode):
        if not node:
            return
        nonlocal answer
        if parent and grandParent and grandParent.val % 2 == 0:
            answer += node.val
        dfs(node.left, node, parent)
        dfs(node.right, node, parent)

    answer = 0
    dfs(root, None, None)
    return answer
#       6
#      / \
#     7   8
#    / \  / \
#   2 7  1   3
#  / / \      \
# 9  1  4       5

# node = 6
# parent = None
# grandparent = None

# node = 7
# parent = 6
# grandparent = None


