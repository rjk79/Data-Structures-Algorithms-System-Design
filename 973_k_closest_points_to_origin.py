# need to import
import math 

def kClosest(points, K):
        res = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            newItem = [point, dist]
            res.append(newItem)

        # return idx into the item
        def sortByDist(item):
            return item[1]
        
        # modifies original
        # pass a key to custom sort
        res.sort(key = sortByDist)
        finalRes = []

        def mapToPoint(item):
            return item[0]

        for i in range(K):
            finalRes.append(res.pop())

        finalRes = map(mapToPoint, finalRes)

        return finalRes

print (kClosest([[1,3],[-2,2]], 1))