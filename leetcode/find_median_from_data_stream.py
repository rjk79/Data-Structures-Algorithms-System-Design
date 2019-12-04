class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap: List[int] = []
        self.max_heap: List[int] = []
        
# [MAX HEAP]  [MIN HEAP]
    def addNum(self, num: int) -> None:
        # push the smallest val in min heap into maxheap
        # pushpop precludes the need to compare inserted val to both heap tops
        # ensures theres no overlap between heap ranges
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        # keep min heap bigger or =
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self) -> float:
        has_even_count = len(self.max_heap) == len(self.min_heap)

        if has_even_count:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(self.min_heap[0])

# min_heap = 1
# max_heap = 

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# O(logn) to insert and remove min