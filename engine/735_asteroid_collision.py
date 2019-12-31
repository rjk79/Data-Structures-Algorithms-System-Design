def asteroidCollision(asteroids):
#  value is size, sign is direction 
# - <= => +
# smaller one explodes
# same size => both explode
        # 9:42
# 5 10
#   -5
# +, - => collide
# +, +  -, -    -, + => no collision

        res = []
        for asteroid in asteroids:
            res.append(asteroid)
            while len(res) > 1 and (res[-2] > 0 and res[-1] < 0): #collisions start happening
                left = res[-2]
                right = res[-1]
                if left > abs(right):
                    res.pop()  
                elif left < abs(right):
                    res.pop(-2)
                elif left == abs(right):
                    res.pop()
                    res.pop()
        return res

a = [5, 10, -5]
b = [8, -8]
c = [10, 2, -5]
print(asteroidCollision(a))
print(asteroidCollision(b))
print(asteroidCollision(c))