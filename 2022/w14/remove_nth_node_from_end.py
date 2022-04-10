# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # case: [1]
        # case: [1, 2] and 1: remove the last el
        # case: [1, 2] and 2: remove the first el (head)
        prev = head
        tail = head
        for _ in range(n):
            tail = tail.next
        if tail is None:
            return prev.next
        while tail.next is not None:
            tail = tail.next
            prev = prev.next
        prev.next = prev.next.next
        return head
