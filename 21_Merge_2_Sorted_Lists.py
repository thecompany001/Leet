class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l2:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        empty = List
        tail = empty
        
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return empty.next