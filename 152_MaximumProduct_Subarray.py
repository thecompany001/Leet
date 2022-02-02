class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp * curMax, n * curMin, n)
            res = max(res, curMax)
        return res