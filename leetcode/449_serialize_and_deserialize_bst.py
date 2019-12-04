
def serialize(root):
        
        def dfs(root):
            if not root:
                return 
            res.append(str(root.val) + ",")
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return "".join(res)

def deserialize(data):
    # root is at [0] 
    # then come values of left subtree [1:k]
    #  then come vals of right subtree [k:]
    def helper(arr, i, j):
        if i > j:
            return
        if i == j:
            node = TreeNode(arr[i])
            return node
        for k in range(i+1, j+1):
            if arr[k] > arr[i]:
                l = helper(arr, i+1, k-1)
                r = helper(arr, k, j)
                root = TreeNode(arr[i])
                root.left = l
                root.right = r
                return root
        l = helper(arr, i+1, j)
        root = TreeNode(arr[i])
        root.left = l
        return root
    
    arr = data.split(",")
    # pop off extra comm
    arr.pop()
    data = [int(x) for x in arr]
    import pdb; pdb.set_trace()
    return helper(data, 0, len(data)-1)

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
a.left = b
a.right = c

serial = serialize(a)
print(deserialize(serial))


# TLE
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []
#         def recurse(root):
#             if not root: return 
#             res.append(str(root.val))
#             if not root.left and not root.right:
#                 return
#             if root.left: 
#                 recurse(root.left)
            
#             if root.right: 
#                 recurse(root.right)
            
#         recurse(root)
#         res = ",".join(res)
#         return res 
            

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
# #       "213"
#         print(data)
#         data = data.split(",")[::-1]
#         if data[0] == "": return 
#         def recurse(lowerBound, upperBound):
#             if not data: return 
#             print(data)
#             currVal = data[-1]
#             if int(currVal) < lowerBound or int(currVal) > upperBound: return      
#             root = TreeNode(int(data.pop()))
#             root.left = recurse(lowerBound, root.val)
#             root.right = recurse(root.val, upperBound)
#             return root
#         return recurse(float('-inf'), float('inf'))
# #     similiar to validate BST