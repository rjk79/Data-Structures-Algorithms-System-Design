nums = 0
def grayCode(n):
    ret = []
    def backTrack(n, ret):
        nonlocal nums
        if (n == 0):
            ret.append(nums)
            return
        
        else:
            backTrack(n - 1, ret)
            nums ^= (1 << n - 1)
            backTrack(n - 1, ret)
    backTrack(n, ret)
    return ret



print(grayCode(3))
# passing info back up the rec stack
# nums = 0
# n = 2
# ret = [0, 01, 11, 10]
# (2)
# 1 ^= 10 == "11"
# (1)
# 0 ^= 1 == "1"
# (0)
# 
# 
# (1)
# 11 ^= 1 == 10
# (0)
# 

# ret = [ 0, 1, 11, 10, 110, 111, 101, 100]
#                    (3)
#   110
# |      \             (2)
# 11         101
# |  \       /     \     (1)
# 1   10    111    100
# |\  | \   |  \    |  \(0)
# 0 1 11 10 110 111 101 100
# 
# 


#      1
# 0  / 0
# 1  \ 0
#      1
