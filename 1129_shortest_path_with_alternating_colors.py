def shortestAlternatingPaths(n, red_edges, blue_edges):
#         11:10 => 26 mins all test cases passed
        redGraph = collections.defaultdict(list)
        blueGraph = collections.defaultdict(list)
        for x, y in red_edges:
            redGraph[x].append(y)
        for x, y in blue_edges:
            blueGraph[x].append(y)
        # print(redGraph, blueGraph)
        res = [float('inf') for _ in range(n)]
        seen = set()
        q = [(0, 0, 2)]
        heapq.heapify(q)
        while q:
            print(q)
            dist, curr, currColor = heapq.heappop(q)
            res[curr] = min(res[curr], dist)
            seen.add((curr, currColor)) #can revisit edges as long as we're coming from a diff color
            if currColor != 0: #not red
                for neigh in redGraph[curr]:
                    if (neigh, 0) not in seen:
                        q.append((dist+1, neigh, 0))
            if currColor != 1: #not blue
                for neigh in blueGraph[curr]:
                    if (neigh, 1) not in seen:
                        q.append((dist+1, neigh, 1))
        def mapRes(el):
            if el == float('inf'):
                return -1
            else:
                return el
        return list(map(mapRes, res))