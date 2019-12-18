def shipWithinDays(weights, D):
        def isPossible(capacity):
            count = 1
            currSum = 0
            for i in range(len(weights)):
#               if we have space
                if currSum + weights[i] <= capacity:
                    currSum += weights[i]
                else:
                    currSum = weights[i]
                    count += 1
            return count <= D
        
        totalW = sum(weights)
#       lowest capacity
        best = float('inf')
        l = 0
        r = totalW + 1
        while l < r:
            mid = (l + r) //2
            if isPossible(mid):
                best = mid
                r = mid
            else:
                l = mid + 1
        return best
print(shipWithinDays([1,2,3,1,1], 4)) #3
