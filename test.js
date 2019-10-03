var copyRandomList = function(head) {
    // edge cases: 0, 1 nodes
    if (!head) return null
    if (!head.next) {
        let newNode = new Node(head.val)
        if (head.random) newNode.random = newNode
        return newNode
    }

    let curr = head
    let clone
    // cant do multiple assignment in JS
    while (curr) {
        clone = new Node(curr.val, null, null)
        clone.next = curr.next
        curr.next = clone
        curr = curr.next.next
    }

    curr = head
    while (curr) {
        // make the clone point to the same thing's clone, if curr has a random assigned
        if (curr.random) curr.next.random = curr.random.next
        curr = curr.next.next
    }
    let cloneHead = head.next

    curr = head
    fast = head.next
    while (curr) {
        curr.next = curr.next.next
        if (fast.next) fast.next = fast.next.next
        curr = curr.next
        fast = fast.next
    }

    

    // curr = head
    // while (curr) {
    //     console.log(`This node is: ${curr.val} with id: ${curr.id}`)
    //     console.log(`It's random is pointing to: ${curr.random.val} with id: ${curr.random.id}`)
    //     curr = curr.next
    // }
    // console.log("done")
    // curr = cloneHead
    // while (curr) {
    //     console.log(`This node is: ${curr.val} with id: ${curr.id}`)
    //     console.log(`It's random is pointing to: ${curr.random.val} with id: ${curr.random.id}`)
    //     curr = curr.next
    // }
    // console.log("done")

    return cloneHead
};



function Node(val, next, random) {
    this.val = val;
    this.next = next;
    this.random = random;
    this.id = null
};

a = new Node(1)
a.id = 1
b = new Node(2)
b.id = 2
a.next = b
a.random = b
b.random = b

copyRandomList(a)