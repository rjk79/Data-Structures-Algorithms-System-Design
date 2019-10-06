def getIntersectionNode(headA, headB):
    l1 = headA
    l2 = headB
    while l1.next:
        while l2.next:
            if l1 == l2: return l1
            l2 = l2.next
        l1 = l1.next
    return None
