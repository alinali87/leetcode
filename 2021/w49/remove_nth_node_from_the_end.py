# Input: head = [1,2,3,4,5], n = 2

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)





class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        counter = 1
        while node.next:
            node = node.next
            counter += 1
        if counter == 1:
            return None
        target = counter - n
        node = head
        head = head if counter != n else head.next
        for _ in range(target - 1):
            node = node.next
        node.next = node.next.next
        return head


s = Solution().removeNthFromEnd(a, 2)

