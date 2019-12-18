require 'byebug'

def flatten(root)

    return nil if !root
#   both missing
    
    if !root.right && !root.left
        return root 
    end
  # left missing
    return root if !root.left
  
#   right missing or both present
    
    if root.right
        oldRight = flatten(root.right)
    end
    root.right = flatten(root.left)
    root.left = nil
    
#   capture the entire thing
    newRightTail = root.right
    while (newRightTail.right)
        newRightTail = newRightTail.right
    end
    if oldRight
        newRightTail.right = oldRight
    end
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
b.left = c

# a.left = b
# a.right = e
# b.left = c
# b.right = d
# e.right = f

flatten(a)

currNode = a
puts "Printing Tree..."
while currNode
    puts currNode.val
    currNode = currNode.right
end


        #     1
        #    / \
        #   2   5
        #  / \   \
        # 3   4   6