from collections import deque

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def create_linked_list(vals):
    temp = Node(-1)
    head = temp

    for val in vals:
        temp.next = Node(val)
        temp = temp.next
    return head.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def create_tree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]):
    if not preorder or not inorder: 
            return None
    node_val = preorder[0]
    index = inorder.index(node_val)

    left_inorder = inorder[:index]
    right_inorder = inorder[index + 1:]

    left_preorder = list(filter(lambda x: x in left_inorder, preorder))
    right_preorder = list(filter(lambda x: x in right_inorder, preorder))

    node = TreeNode(node_val)
    node.left = create_tree(left_preorder, left_inorder)
    node.right = create_tree(right_preorder, right_inorder)
    return node

def print_tree(root):
    def get_depth(node):
        if not node: return 0
        return max(get_depth(node.left), get_depth(node.right)) + 1
    
    def insert_value(node, lo, hi, depth=0):
        if not node: return
        mid = (lo + hi) // 2
        output[depth][mid] = str(node.val)
        insert_value(node.left, lo, mid, depth + 1)
        insert_value(node.right, mid, hi, depth + 1)

    depth = get_depth(root)
    output = [[""] * (2**depth - 1) for _ in range(depth)]
    
    insert_value(root, 0, 2**depth - 1)
    # return output
    for res in output:
        print(res)

def preorder_print(root):
    print(root.val)
    if root.left:
        preorder_print(root.left)
    if root.right:
        preorder_print(root.right)

def postorder_print(root):
    if root.left:
        postorder_print(root.left)
    if root.right:
        postorder_print(root.right)
    print(root.val)

def inorder_print(root):
    if root.left:
        inorder_print(root.left)
    print(root.val)
    if root.right:
        inorder_print(root.right)
    
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}