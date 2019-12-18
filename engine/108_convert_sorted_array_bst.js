var sortedArrayToBST = function (nums) {
    if (!nums.length) return null

    let midIdx = Math.floor(nums.length / 2)
    let root = new TreeNode(nums[midIdx])
    root.left = sortedArrayToBST(nums.slice(0, midIdx))
    root.right = sortedArrayToBST(nums.slice(midIdx + 1))

    return root
};
// find median
// 0 => null
// 
// 3 things => 1
// 4 things => 1, 2 => 1
// work outwards, maybe 2 at a time
// if theres nothing there then thats ok
// 0 things, one thing