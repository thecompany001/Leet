class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur