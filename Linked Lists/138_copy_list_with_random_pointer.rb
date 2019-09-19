
# clone
# head
# 1		1’		2		2’		3		3’		4		4’	
# runner1	runner2
# dummy1	dummy2


# step 1 
# make clones between every node

# step 2
# set up the random pointers
# make the clone.random = the real node’s random except 1 more node away (so it hits clone instead)
# curr.next.random = curr.random.next

# step 3
# fix all .next of all nodes
# runner1.next  = runner1.next.next
# runner2.next = runner2.next.next
