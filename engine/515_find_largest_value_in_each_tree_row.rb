def largest_values(root)
    return [] if !root
    q = [root]
    res = []
    while q.length != 0
        res << q.map{|node| node.val}.max
        newQ = []
        q.each{|node| 
            newQ << node.left if node.left
            newQ << node.right if node.right
        }
        q = newQ
    end
    res
end
# keep clearing the queue and fill it with child nodes