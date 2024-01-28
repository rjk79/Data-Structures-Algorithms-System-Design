from helpers import create_linked_list, ListNode, print_list

def reverse(head):
    prev = None
    curr = head
    third = head.next

    while curr:
        third = curr.next
        curr.next = prev
        prev, curr = curr, third
    return prev

head = create_linked_list([1,2,3,4,5])

new_head = reverse(head)
print_list(new_head)
