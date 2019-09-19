# each node is the max of the subtree
def construct_maximum_binary_tree(nums)
    return nil if nums.length == 0
    max = nums.max  
    maxIndex = nums.index(max)
    newNode = TreeNode.new(max)
    newNode.left = construct_maximum_binary_tree(nums[0...maxIndex])
    newNode.right = construct_maximum_binary_tree(nums[maxIndex+1..-1])
    return newNode
end