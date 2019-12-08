
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    dp = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and dp[i] < dp[j] + 1 : 
                dp[i] = dp[j]+1
  

    # find max of all 
    
  
    return max(dp)
print(lis([3, 10, 2, 1, 20])) #3
print(lis([50, 3, 10, 7, 40, 80])) #4


# 0 1 2 3 4 
# 1 2 1 1 3 

# 1, 5

# i 1 | 2   | 3     | 4
# j 0 | 0 1 | 0 1 2 | 0 1 2 3 
# 

# print(lis([50, 3, 10, 7, 40, 80])) #4


# def optim(arr):
#     n = len(arr)
#     dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if arr[j - 1] > arr[i - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1 #leftup + 1
#             else:
#                 dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) #max of left and up
#     return dp[-1][-1]



# arr = [5, 8, 3, 7, 9, 1]
# print(optim(arr))