def isHappy(n):
        def helper(num):
            sum = 0
            while num > 0:
#  last digit, ones place
                sum += (num % 10)**2
                num /= 10
            return sum
        
        slow = n
        fast = helper(n)
        while slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        return slow == 1

print (isHappy(19))

# 19 => 82 => 68 => 85 => 89 => 145 => 42 => 20 => 4 => 16 => 37 => 58 => 65 => 41 => 17 => 50 => 25 => 29 => 85