from helpers import create_tree, print_tree

from collections import deque

def connect(root):
    #level order traversal
    #for each node point to the next one
    queue = deque([root])
    
    while queue:
        length = len(queue)
        for _ in range(length):
            curr = queue.popleft()
            if queue:
                curr.next = queue[0]
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

tree = create_tree()
print_tree(tree)
connect(tree)
        


