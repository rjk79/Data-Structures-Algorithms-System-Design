# constant space
# n time
# nil is nothing in ruby

def odd_even_list(head)
# 0 nodes
    if !head
        return nil
# 1 node
    elsif !head.next
        return head
# 2 nodes
    elsif !head.next.next
        return head
    end
# 3+ nodes
    currEven = head
    currOdd = head.next
    
    oddHead = head.next
    currNode = head.next.next
    
    while currNode
        currEven.next = currNode
        currEven = currEven.next
        currNode = currNode.next
        # puts currEven.val

        if currNode
            currOdd.next = currNode
            currOdd = currOdd.next
            currNode = currNode.next
            # puts currOdd.val
        end
    end
    currOdd.next = nil
    currEven.next = oddHead
    
    printNode = head
    while printNode
        puts printNode.val
        printNode = printNode.next
    end
    return head
    
end

# keep track of a currEven and a currOdd
# alternate linking them to new nodes
# but never lose track of head of even nodes
# so u can link it to end of odd chain