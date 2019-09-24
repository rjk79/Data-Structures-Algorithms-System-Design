
def copyRandomList(head):
    if not head: return None
    
    curr = head
    cloneNode = Node(head.val, None, None)
    cloneHead = cloneNode
    
    if not head.next: return cloneHead

    curr.next, cloneNode.next = cloneNode, curr.next
    curr = cloneNode.next
#       weave clone nodes in
    while curr:
        cloneNode = Node(curr.val, None, None)
        curr.next, cloneNode.next = cloneNode, curr.next
        curr = cloneNode.next
#       set the random pointers for clones
    curr = head
    cloneCurr = head.next
    while curr:
        cloneCurr.random = curr.random.next
        curr = curr.next.next
#       extract the clone nodes
    curr = cloneHead
    while curr:
        curr.next = curr.next.next
        curr = curr.next.next
        
    return cloneHead

    class Node:
        def __init__(self, val, next, random):
            self.val = val
            self.next = next
            self.random = random




# clone
# head
# 1		1		2		2		3		3		4		4
# runner1	runner2
# dummy1	dummy2


# step 1 
# make clones between every node

# step 2
# set up the random pointers
# make the clone.random = the real nodes random except 1 more node away (so it hits clone instead)
# curr.next.random = curr.random.next

# step 3
# fix all .next of all nodes
# runner1.next  = runner1.next.next
# runner2.next = runner2.next.next

