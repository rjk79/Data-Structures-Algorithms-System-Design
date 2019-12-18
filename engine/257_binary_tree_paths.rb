def binary_tree_paths(root)
    return nil if !root
    return ["#{root.val}"] if !root.right && !root.left 
#   [ [], [], [] ]
    if root.right && root.left
        prev = binary_tree_paths(root.right).concat( binary_tree_paths(root.left) )
    elsif root.right && !root.left
        prev = binary_tree_paths(root.right)
    elsif root.left && !root.right
        prev = binary_tree_paths(root.left)
    end
    prev.map!{|path|
        "#{root.val}->" + path
    }
    return prev
    
end

# 1->2->5
# 1->3


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

    #     1
    #    / \
    #   2   3
    #    \
    #     5

a.left = b
a.right = c
b.right = e

print binary_tree_paths(a)
