# Odd/Even, work in reverse

# case: x = 2, y = 8

# worst case u end up at 14 which is 2*(y-1) AKA jumpMax
# b/c you wouldnt blaze past 8 and go to 16..

# 2 ways to get to y


# double
# m = y/2
#  -or-
# decrement
# 2m + 1 -> anything times 2 and plus 1 is ODD

# so had to come from 2m + 2 which is EVEN -> can also be accessed via double or dec
# if we had dec then we'd come from 2m + 4 which is 2(m + k)
# AKA 8 can be gotten from
# 5 * 2 - 1 - 1 (3 steps) OR 
# 5 - 1 * 2 (2 steps => better)

# conclusion:
# even nums are best accessed via doubling
# odd                accessed via decrement

def brokenCalc(X, Y):
    import pdb; pdb.set_trace()

    if X == Y: return 0
    if X > Y:
        return X - Y
    elif X <= Y:
        if Y % 2 == 0:
            return 1 + brokenCalc(X, Y/2)
        else:
            return 1 + brokenCalc(X, Y+1)

brokenCalc(5, 8)