# need fake node at start to remove head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#       edge: 1 node list
        if not head.next:
            return None
#       we're deleting the thing after so stop 1 early
#       removing 2nd node means moving prev
        prev = ListNode(0)
        prev.next = head
        lead = head
        moved = False
#       starting the prev at head prevents deleting head
       
        for x in range(n):
            lead = lead.next

#       offset the lead
        while lead:
            prev = prev.next
            lead = lead.next
            moved = True

#       lead will make it to tail
        prev.next = prev.next.next
        if not moved:
            return prev.next
        return head
     