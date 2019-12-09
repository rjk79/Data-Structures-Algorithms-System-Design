def subarraysDivByK(A, K):
    res = 0
    prefix = 0
    count = [1] + [0] * K
    for a in A:
        prefix = (prefix + a) % K
        res += count[prefix]
        count[prefix] += 1
    return res

print(subarraysDivByK([4,5,0,-2,-3,1], 5))
# [4,5,0,-2,-3,1], K = 5 #7
# res = 0 1 3 6 7
# prefix = 0 4 4 4 2 4 0
# count = [2 0 1 0 4 0]
# a = 4 5 0 -2 -3 1

# if we count up, hit a num with remainder X, count up, then hit a bigger num with remainder X
# then the difference between them must be a num divis by K
# we go up by the amount prefix[remainder] because that is how we grow/calc # of subarrays 

# 10 5 5    K = 5
# res = 0 1 3 6

# 10 5 3 2 5 K =5
# res = 0 1 3 6 10 
# the second 5 sees 3 other things it can interact with: 10, 5, 3+2
