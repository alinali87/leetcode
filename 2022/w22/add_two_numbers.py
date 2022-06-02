# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        prev = ListNode(0)
        head = prev
        add = 0
        while node1 and node2:
            val = node1.val + node2.val + add
            add = val // 10
            val = val % 10
            node = ListNode(val)
            prev.next = node
            prev = node
            node1 = node1.next
            node2 = node2.next
        while node1:
            val = node1.val + add
            add = val // 10
            val = val % 10
            node = ListNode(val)
            prev.next = node
            prev = node
            node1 = node1.next
        while node2:
            val = node2.val + add
            add = val // 10
            val = val % 10
            node = ListNode(val)
            prev.next = node
            prev = node
            node2 = node2.next
        if add > 0:
            node = ListNode(add)
            prev.next = node
        head = head.next
        return head
