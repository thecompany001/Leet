#DFS

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(q.left, q.right))
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, p.right) and 
               self.isSameTree(q.right, q.right))
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isTreeSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False

        return (self.isTreeSame(p.left, p.right) and
               self.isTreeSame(q.left, q.right))
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isTreeSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isTreeSame(p.left, p.right) and
               self.isTreeSame(q.left, q.right))
    

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.right) and
               self.isSameTree(q.left, q.right))
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val
            return False
        
        return (self.isSameTree(p.left, p.right) and
               self.isSameTree(q.left, q.right))
    
    

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val!= q.val:
            return False
        
        return (self.isSameTree(p.left, p.right) and
               self.isSameTree(q.left, q.right))
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, p.right) and
               self.isSameTree(q.left, q.right))
    
    

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, p.right) and
               self.isSameTree(q.left, q.right))
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def isTreeSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p or not q or p.val != q.val:
            return False
        return (self.isTreeSame(p.left, p.right) and
               self.isTreeSame(q.left, q.right))
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def 
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):