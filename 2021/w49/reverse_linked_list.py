from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        buf = [node.val]
        while node.next:
            buf.append(node.next.val)
            node = node.next
        node = head
        for i in range(len(buf)):
            node.val = buf[len(buf) - 1 - i]
            node = node.next
        return head
