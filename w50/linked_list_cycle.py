class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        m = set([head])
        node = head
        while node.next:
            if node.next in m:
                return True
            m.add(node.next)
            node = node.next
        return False