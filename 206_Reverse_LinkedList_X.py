# Iterative
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



# Recursive
class Solution(object):
    def reverseList(self, head):
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Iterative
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    
# Recursive
class Solution(object):
    def reverseList(self, head):
    
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead
    
    
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Iterative
class Solution(object):
    def reversalList(self, head):
        prev, cur = None, head
        
        while curr:
            nxt: curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    
    
    
    
    
    
# Recursive
class Solution(object):
    def reverseList(self, head):
        
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead
    
    
    
    
    
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Iterative
class Solution(object):
    
    
    
    
    
    
    
# Recursive
class Solution(object):
    
    
    
    
    
    
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Iterative
class Solution(object):
    
    
    
    
    
    
    
# Recursive
class Solution(object):