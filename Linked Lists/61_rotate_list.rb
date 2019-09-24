def rotate_right(head, k)
    return nil if !head
    return head if k == 0
    
    count = 0
    curr = ListNode.new(0)
    curr.next = head
#   find length
    while curr.next
        curr = curr.next
        count += 1
    end
#   loops the list
    curr.next = head
#   curr is at tail
    
    
    curr = head
    lead = curr.next
#   curr at 3, lead at 4
#   2 % 5 = 2
    (k % count).times {
        curr = curr.next
        lead = lead.next
        }
    curr.next = nil
    
    lead
    
end
# reset pointer lead pointer if k would cause it to go off the list
# dont need dummy head

