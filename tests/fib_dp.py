def function(n):
    if n == 1 or n == 2: return 1
    return function(n - 1) + function(n - 2)

# 2^n


print(function(7))
# n
def recurse(n):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        # import pdb; pdb.set_trace()
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
    
print(recurse(7))


    # [1 1 2 3 5]
        #  function(5)
        # / \
        # f(3)  f(4)
        # /\ /\
        #1 2 2 3
            #  /\
            #  1 2  
           
# 1 1 2 3 5 8 13 