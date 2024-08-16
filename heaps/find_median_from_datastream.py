'''
295: HARD
Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the 
data stream to the data structure.
- double findMedian() returns the median of all 
elements so far. 
'''

import heapq
class MedianFinder:
    # time - O(logn), space - O(1)
    def __init__(self):
        self.low = []
        self.high = []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, - num)
        heapq.heappush(self.high, - heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, - heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.high) == len(self.low):
            return (- self.low[0] + self.high[0])/2
        return - self.low[0]