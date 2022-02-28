class MedianFinder(object):

    def __init__(self):
        #two heaps, large, small, minheap, maxheap
        #heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num):
        heapq.heappush(small, -1 * num)
        
        #make sure every num small is <= every num in large
        if (small and large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
            #uneven size?
            if len(small) > len(large) + 1:
                val = heapq.heappush(self.large)
                
        

    def findMedian(self):
        