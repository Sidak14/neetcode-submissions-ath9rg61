# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        cur = slow.next
        slow.next = None
        nxt = cur.next
        cur.next = None
        while nxt:
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp
        
        l1 = head
        l2 = cur
        while l1 and l2:
            temp = l1.next
            l1.next = l2
            l1 = temp
            temp = l2.next
            l2.next = l1
            l2 = temp
