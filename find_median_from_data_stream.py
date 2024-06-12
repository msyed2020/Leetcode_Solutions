import heapq

'''
Find Median From Data Stream poses the question of finding the median value from an ordered list. There is no legitimate
middle value, as the lists are even. Therefore, the mean is the middle two values added together and divided by 2 (since
in this problem, we want the middle TWO values always, we can hard divide by 2). What we actually need to do, according
to this class, is to extract the values and actually add them to a data structure.

To do this, we can use a minHeap and a MaxHeap, that way the values can be easily extracted within efficient time. The
small heap is actually the MaxHeap, as small represents the max from the first half, and the large is the minHeap, which
is the min from the second half.
 
'''

class MedianFinder:

    def __init__(self):
        # initialize small and large heaps
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # add num to maxHeap. Multiply by -1 since heapq is default a minHeap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # if the largest number in small is bigger than the smallest number in large, move said number to large
            # and maintain order
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            # If small has more than one extra element as compared to large, move the root of small to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # If large has more than one extra element as compared to small, move the root of large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

     def findMedian(self) -> float:
        if len(self.small) > len(self.large): # if small has more elements than large, return small's root value (if odd)
            return -1 * self.small[0]
        if len(self.large) > len(self.small): # if large has more elements than small, return large's root value (if odd)
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2 # otherwise, return the median values as expected and described
    # above
