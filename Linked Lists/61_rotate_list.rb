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

class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

a = ListNode.new(1)
b = ListNode.new(2)
c = ListNode.new(3)
d = ListNode.new(4)
e = ListNode.new(5)
a.next = b
b.next = c
c.next = d
d.next = e

rotate_right()
# reset pointer lead pointer if k would cause it to go off the list
# dont need dummy head

