def flatten(root)
    return nil if !root
#   both missing
    
    if !root.right && !root.left
        return root 
    end
    # left missing
    return root if !root.left
#   right missing
    if !root.right && root.left
        root.right = root.left
        root.left = nil
    end

#   both present
    
    currRight = flatten(root.right)
    root.right = flatten(root.left)
    root.left = nil
    root.right.right = currRight
    
    return root
end

class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

a = TreeNode.new(1)
b = TreeNode.new(2)
c = TreeNode.new(3)
d = TreeNode.new(4)
e = TreeNode.new(5)
f = TreeNode.new(6)

a.left = b
a.right = e
b.left = c
b.right = d
e.right = f

flatten(a)

currNode = a
puts "Printing Tree..."
while currNode
    puts currNode.val
    currNode = currNode.right
end