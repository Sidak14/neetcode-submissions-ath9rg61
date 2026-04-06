"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        hashmap = {}
        cur = head
        prev = None
        while cur:
            hashmap[cur] = Node(cur.val)
            if prev:
                hashmap[prev].next = hashmap[cur]
            prev = cur
            cur = cur.next
        
        cur = head
        while cur:
            if cur.random:
                hashmap[cur].random = hashmap[cur.random]
            cur = cur.next
        
        return hashmap[head]

        