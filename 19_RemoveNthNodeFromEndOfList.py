class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNodE(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            
        #delete 
        left.next = left.next.next
        return dummy.next