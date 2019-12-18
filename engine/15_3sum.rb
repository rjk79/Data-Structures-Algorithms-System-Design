require 'byebug'
def three_sum(nums)
    res = []
    nums = nums.sort
    i = 0
    while i < nums.length - 2
        left = i + 1
        right = nums.length - 1
        until left == right
            if nums[i] + nums[left] + nums[right] === 0
                sub = [nums[i], nums[left], nums[right]]
                res << sub 
                oldLeft = left
                while nums[oldLeft] == nums[left] && left != right
                    left += 1
                end
            elsif nums[i] + nums[left] + nums[right] > 0
                right -= 1
            elsif nums[i] + nums[left] + nums[right] < 0
                left += 1
            end
        end
        
        oldI = i
        while nums[oldI] == nums[i]
            i += 1
        end
    end
    
    
    
    res
end

# same as two-sum with 2 pointers except
# i moves up to constrict movement of 2 pointers
three_sum([-1,0,1,2,-1,-4])