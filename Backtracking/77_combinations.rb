# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# order doesnt matter so recur calls form triangle
# AKA no repeats

# like permutations except constrained by size

# n is the integer youre going up to
# k is the # of things in each combin. 
var combine = function(n, k) {
    let nums = []
    # reformat input
    for (let i = 1; i <= n; i++) {nums.push(i)}
    let res = []

    function recurse(curr, k, start) {
        # returns at a certain point -> base case
        if (k == 0) {
            res.push(curr.slice(0))
            return  
        }
        
        let i = start
        while (i < nums.length){
            curr.push(nums[i])
            recurse(curr, k - 1, i + 1)
            curr.pop()
            i+=1 
        }
            
    }
        
    recurse([], k, 0)
    return res
  
};




def combine(n, k)
    nums = (1..n).to_a
    res = []

#   current prod and iterator
#   ruby needs to pass res and nums eventho theyd be in-scope for js/py
    def recurse(curr, k, nums, res, start)
#   add, recurse, undo
        # basically forcing a base case
        if k == 0
            res << curr[0..-1] 
            return
        end
        # start elims duplicates (like [3, 2] [2, 3])
        i = start
        while i < nums.length
            curr << nums[i]
            recurse(curr, k - 1, nums, res, i + 1)
            curr.pop
            i+=1
        end
        
    end
    recurse([], k, nums, res, 0)
    res
end

