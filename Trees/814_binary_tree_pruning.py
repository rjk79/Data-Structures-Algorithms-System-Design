

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if (root.left):
            root.left = self.pruneTree(root.left)
        if (root.right):
            root.right = self.pruneTree(root.right)
        if (not(root.left) and not(root.right) and root.val == 0):
            return None
        else:
            return root
