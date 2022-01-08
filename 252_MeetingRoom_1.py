class Solution:
    intervals.sort(key = lambda i : i.start)
    
    for i in range (1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]
        
        if i1.end > i2.end:
            return False
    return True
    
    