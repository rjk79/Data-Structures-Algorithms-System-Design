class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        q = []
        def recurse(root): #inorder
            if root.left: recurse(root.left)
            q.append(root)
            if root.right: recurse(root.right)
        recurse(root)
        for i in range(len(q)): #for each node
            q[i].left = q[i - 1] 
            if i == len(q) - 1:
                q[i].right = q[0]
            else:
                q[i].right = q[i+1]
        return q[0]
                
#   inorder traversal