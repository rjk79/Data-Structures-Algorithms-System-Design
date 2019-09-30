# def rotateRight(self, head, k):
#         n, pre, current = 0, None, head
#         while current:
#             pre, current = current, current.next
#             n += 1
                            # current falls off, pre becomes tail, n is length

                            # if length is 0 or we are rotating only to end up back where we started 

#         if not n or not k % n:
#             return head
                            # 5 things, 7 rotations --> 2 net
                            # 5 - 2 - 1 = 2
                            # (i.e. 5 - 7 % 5 - 1 )

                            # 3 things, 1 rotations --> 1 net
                            # 3 - 1 - 1 = 1
                            
                            # 3 things, 2 rotations --> 2 net
                            # 3 - 2 - 1 = 0 (MOVE 0 TIMES)

                            # moving "tail" up so it becomes at the new tail
#         tail = head
#         for _ in xrange(n - k % n - 1):
#             tail = tail.next


                            # pre is at tail so make it bite the head
#         next, tail.next, pre.next = tail.next, None, head
#         return next

                            # 0 -> 1 -> 2

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
# c = ListNode.new(3)
# d = ListNode.new(4)
# e = ListNode.new(5)
a.next = b
# b.next = c
# c.next = d
# d.next = e

rotate_right(a)
# reset pointer lead pointer if k would cause it to go off the list
# dont need dummy head

