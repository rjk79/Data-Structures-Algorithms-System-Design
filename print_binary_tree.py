# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]

def printTree(root):

    def get_height(node):
        return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
    
    def update_output(node, row, left, right):
        if not node:
            return
        mid = (left + right) / 2
        self.output[row][mid] = str(node.val)
        update_output(node.left, row + 1 , left, mid - 1)
        update_output(node.right, row + 1 , mid + 1, right)
        
    height = get_height(root)
    width = 2 ** height - 1
    self.output = [[''] * width for i in xrange(height)]
    update_output(node=root, row=0, left=0, right=width - 1)
    return self.output

# height = 3
# width = 7
# self.output = 
# ['', '', '', '1', '', '', '']
# ['', '2', '', '', '', '3', '']
# ['', '', '4', '', '', '', '']

# node =  1
# row =   0
# left =  0
# right = 6
# mid = 3
# [row][mid] = val

# 2
# row = 1
# left = 0 (left)
# right = 2 (mid - 1)
# mid = 1

# 3
# row = 1
# left = 4 (mid + 1)
# right = 6 (right)
# mid = 5

# 4
# row = 2
# left = 2 (mid + 1)
# right = 2
# mid = 2