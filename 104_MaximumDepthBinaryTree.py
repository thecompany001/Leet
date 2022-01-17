#DFS - Recursion

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), max(self.maxDepth(node.right))
    
    
    
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
                       

        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
                       
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
                       
                       
                       
                       
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    

class Solution(object):
    def maxDepth(self, root):
    
    
    
    
#DFS - Recursion
    
    
    
    
#DFS - Iterative
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
                       
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
            


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        stack = ([root, 1])
        res = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack. append([node.right, depth +1])
        return res


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        stack = ([root, 1])
        res = 0
        
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        
        
        
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:

        
        
#DFS - Iterative

#BFS

class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                       q.append(node.left)
                if node.right:
                       q.append(node.right)
            
            level += 1
        return level


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
                       
                       
                       
          
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
                       
                       
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:


 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:


#BFS