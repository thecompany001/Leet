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
    


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root and subRoot: return False
        
        if self.sameTree(root, subroot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and t and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
            


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def isSubtree(self, root, subRoot):



        
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def isSubtree(self, root, subRoot):







XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def isSubtree(self, root, subRoot):


