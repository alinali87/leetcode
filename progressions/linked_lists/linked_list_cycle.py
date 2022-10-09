from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast is slow:
                return True
        return False
