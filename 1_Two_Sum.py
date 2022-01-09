class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

List [2, 1, 5, 3]


class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = 1
        return


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]
        prevMap = {}

        for i in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = 1
        return
