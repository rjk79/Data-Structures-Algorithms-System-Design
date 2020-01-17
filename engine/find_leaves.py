def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        while root:
            leaves = []
            def dfs(node):
                if not node.left and not node.right: 
                    leaves.append(node.val)
                    return None
                if node.left: 
                    node.left = dfs(node.left)
                if node.right: 
                    node.right = dfs(node.right)
                return node
            root = dfs(root)
            res.append(leaves)
        

        return res