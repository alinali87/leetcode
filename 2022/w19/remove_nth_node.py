# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        for _ in range(n - 1):
            node = node.next
        target = head
        prev = None
        while node.next:
            prev = node
            node = node.next
            target = target.next
        # node is tail
        # target must be deleted
        # target is tail, target is head, is in between
        if target is node:
            if prev:
                prev.next = None
                return head
            else:
                return None
        target.val = target.next.val
        target.next = target.next.next
        if target is head:
            return target
        return head


