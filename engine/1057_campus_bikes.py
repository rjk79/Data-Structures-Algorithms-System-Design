def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
# find dist of each worker from bike 
        q = []
        for i1, worker in enumerate(workers):
            for i2, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                q.append((dist, i1, i2))
        q.sort()
# [distance, worker, bike]
        res = [None for _ in range(len(workers))]
# heap for each worker. heaps w/in heap
        assignedBikes = set()
        assignedWorkers = set()
        for dist, worker, bike in q:
            if worker not in assignedWorkers and bike not in assignedBikes:
                res[worker] = bike
                assignedBikes.add(bike)
                assignedWorkers.add(worker)
        return res