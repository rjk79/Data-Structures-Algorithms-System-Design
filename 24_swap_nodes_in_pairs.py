def swapPairs(head):
        if not head or not head.next: return head
        prev = ListNode(0)
        newHead = prev 
        curr = head
        prev.next = head
        while prev.next and prev.next.next:
            third = curr.next
            prev.next, curr.next, third.next = third, third.next, curr
            prev = curr
            curr = prev.next
        
        
        
        return newHead.next
#   1 2 3 4 
# p c t
#   2 1 3 4
# p t c
#     p c

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

resHead = swapPairs(a)

while resHead:
    print(resHead.val)
    resHead = resHead.next

