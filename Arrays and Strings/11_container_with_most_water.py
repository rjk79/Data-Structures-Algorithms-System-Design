# class Solution:
def maxArea(height):
    max = 0
    # two pointers (idx's)
    i = 0
    j = len(height) - 1
    while not i == j:
        volume = min( height[i], height[j] ) * (j - i)
        if volume > max: max = volume
        if height[i] > height[j]: 
            j -= 1
            # j come closer
        else:
            i += 1
            # i move up
    return max

# LOGIC: you want to move inwards to see if its worth finding a higher wall
#        but you always want to move the lower of the walls
#        b/c if you moved the higher one, it wouldnt matter even if u found a higher wall 
#        youd be limited by your old lower one

print maxArea([1,8,6,2,5,4,8,3,7])