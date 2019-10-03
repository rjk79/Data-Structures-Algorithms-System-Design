# def minimumTotal(triangle):
#     memo = {}
#     def recurse (point):     
#         m, n = point
#         if (m < 0 or m >= len(triangle) or n < 0 or n >= len(triangle[m])):
#             import pdb; pdb.set_trace()
#             return 0
#         if '{m+1}, {n}' in memo:
#             left = memo['{m+1}, {n}']  
#         else:
#             left = recurse([m+1, n])
#         right = memo['{m+1}, {n+1}'] if '{m+1}, {n+1}' in memo else recurse([m+1, n+1])
#         memo['{m}, {n}'] = triangle[m][n] + min(left, right)
#         return memo['{m}, {n}']

#     return recurse([0, 0])

def minimumTotal(triangle):
        for m in reversed(range(len(triangle) - 1)):
            for n in range(len(triangle[m])):
                if triangle[m+1][n]:
                    left = triangle[m+1][n]
                else:
                    left = 0
                if triangle[m+1][n + 1]:
                    right = triangle[m+1][n + 1]
                else:
                    right = 0
                triangle[m][n] = min(left, right) + triangle[m][n]
        return triangle[0][0]
    

print (minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))