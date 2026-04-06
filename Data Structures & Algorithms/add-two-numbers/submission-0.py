# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        cur1 = l1
        cur2 = l2
        carry = 0
        newHead = None
        cur = None
        while cur1 and cur2:
            total = cur1.val + cur2.val + carry
            carry = total // 10
            total = total % 10
            temp = ListNode(total)
            if cur:
                cur.next = temp
            else:
                newHead = temp
            cur = temp
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            total = cur1.val + carry
            carry = total // 10
            total = total % 10
            temp = ListNode(total)
            if cur:
                cur.next = temp
            cur = temp
            cur1 = cur1.next
        
        while cur2:
            total = cur2.val + carry
            carry = total // 10
            total = total % 10
            temp = ListNode(total)
            if cur:
                cur.next = temp
            cur = temp
            cur2 = cur2.next
        
        if carry:
            cur.next = ListNode(carry)

        return newHead
