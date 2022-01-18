class Solution(object):
    def isSubtree(self, root, subRoot):
        if not t:
            return True
        if not s: 
            return False
        
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or
        self.isSubtree(s.right, t))
        
        
        
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
        
        return False