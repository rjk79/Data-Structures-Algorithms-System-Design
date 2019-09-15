
var reverseBetween = function (head, m, n) {
    if (head === null) return null
    if (m === n) return head

    let prev = { val: null, next: head }
    let curr = head
    //     moves m - 1 times but hits 0 either way
    // if m = 3, would console log "2, 1" instead of "2, 1, 0"
    // decrements before checking in "while"
    while (--m) {
        prev = prev.next
        curr = curr.next
        n--
    }
    let con = prev
    let tail = curr
    if (curr.next !== null) {
        prev = prev.next
        curr = curr.next
    }


    let third;
    while (--n) {
        third = curr.next
        curr.next = prev
        prev = curr
        curr = third
    }

    //check if nothing precedes reversed list
    con.val == null ? head = prev : con.next = prev
    tail.next = curr
    // console.log(con);
    // console.log(tail)
    // console.log(prev)
    // return con.val ? head : con.next;
    return head
};