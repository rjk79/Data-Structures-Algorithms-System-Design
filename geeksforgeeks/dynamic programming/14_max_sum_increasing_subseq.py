def maxSumIS(arr, n): 
    max = 0
    dp = [0 for x in range(n)] 
  
    # Initialize dp values 
    # for all indexes 
    for i in range(n): 
        dp[i] = arr[i] 
 
    # values in bottom up manner 
    for i in range(1, n): 
        for j in range(i): 
            # number to Right needs to be larger
            if (arr[i] > arr[j] and
            # if it sets a new record
                dp[i] < dp[j] + arr[i]): 
                dp[i] = dp[j] + arr[i] 
  
    # Pick maximum of 
    # all dp values 
    for i in range(n): 
        if max < dp[i]: 
            max = dp[i] 
  
    return max

    {1, 101, 2, 3, 100, 4, 5}, then output should be 106