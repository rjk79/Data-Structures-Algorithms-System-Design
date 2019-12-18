def lcaDeepestLeaves(self, root):
    def helper(root):
        if not root: return 0, None
        h1, lca1 = helper(root.left)
        h2, lca2 = helper(root.right)
        if h1 > h2: return h1 + 1, lca1
        if h1 < h2: return h2 + 1, lca2 #if a node comes from a deeper sutree return it
        return h1 + 1, root #resolve the tie with ourselves
    return helper(root)[1]


#         1        2,1
#        / \       / \
#       2   3    1,2  1,3
#         1              3,4
#        / \            /  \
#       2   3         2,4   1,3
#      /             /
#     4            1,4
#         1               3,2
#        / \             /  \
#       2   3          2,2   1,3
#      / \            /  \
#     4   5         1,4   1,5