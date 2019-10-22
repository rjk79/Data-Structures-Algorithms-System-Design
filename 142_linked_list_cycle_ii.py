# [3,2,0,-4]
# 1
# cycle size of 3

# slow 2 fast 0
# slow 0 fast 2
# slow -4 fast -4

def detectCycle(self, head: ListNode) -> ListNode:
#       0, 1 nodes
        if (not head) or (not head.next) or (not head.next.next): return None
        slow = head
        fast = head
#       wont check for fast.next.next if fast.next == None
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
#           when they meet, set one to head and move both up slowly 
            if slow == fast: 
                slow = head
                while slow == fast:
                    slow.next, fast.next = slow.next, fast.next       
                return slow
        
        return None