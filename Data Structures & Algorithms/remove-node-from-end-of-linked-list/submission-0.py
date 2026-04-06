# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        cur = head
        while cur:
            cur = cur.next
            sz += 1
        
        print(sz)
        index = sz - n
        currentIndex = 0
        prev = None
        cur = head
        while currentIndex < index:
            prev = cur
            cur = cur.next
            currentIndex += 1

        if not prev:
            return cur.next
        
        prev.next = cur.next
        return head
