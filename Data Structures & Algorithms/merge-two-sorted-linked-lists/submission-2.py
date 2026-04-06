# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        if not list1:
            return list2
        if not list2:
            return list1
        
        l1 = list1
        l2 = list2
        
        head = l1
        if l2.val < l1.val:
            head = l2

        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1.next
                if not temp or temp.val > l2.val:
                    l1.next = l2
                l1 = temp
                continue
            
            # l2.val < l1.val
            temp = l2.next
            if not temp or temp.val >= l1.val:
                l2.next = l1
            l2 = temp
        
        return head
