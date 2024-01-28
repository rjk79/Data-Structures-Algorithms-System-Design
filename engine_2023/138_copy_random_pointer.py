from helpers import create_linked_list, Node, print_list

def copyRandomList(head):
    #map original to copy
    #iter through dic. assign 'next' pointers and 'random' pointers
    hash_map = {}

    curr = head
    
    while curr:
        hash_map[curr] = Node(curr.val)
        curr = curr.next
    
    for node, new_node in hash_map.items():
        if node.next:
            new_node.next = hash_map[node.next]
        if node.random:
            new_node.random = hash_map[node.random]
    print_list(hash_map[head])
    return hash_map[head]

case = create_linked_list([7, 13, 11, 10, 1])
print(copyRandomList(case))