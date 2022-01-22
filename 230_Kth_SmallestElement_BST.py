class Solution(object):
    def kthSmallest(self, root, k):
        n = 0
        stack = []
        cur = root
        
        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val