# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = n - 1
        target = head
        mobile_tail = head
        for _ in range(diff):
            prev = mobile_tail
            mobile_tail = mobile_tail.next
        while mobile_tail.next is not None:
            prev = mobile_tail
            mobile_tail = mobile_tail.next
            target = target.next
        if mobile_tail is head:
            return None
        if target.next:
            target.val = target.next.val
            target.next = target.next.next
        else:
            prev.next = None
        return head
