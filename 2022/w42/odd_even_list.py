from typing import Optional
import utils


class Solution:
    def oddEvenList(self, head: Optional[utils.ListNode]) -> Optional[utils.ListNode]:
        # grow odd
        # grow even
        # chain even after odd
        c = 0
        dummy_odd = utils.ListNode()
        odd = dummy_odd
        dummy_even = utils.ListNode()
        even = dummy_even
        node = head
        while node:
            buf = node.next
            node.next = None
            if c % 2 == 0:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            node = buf
            c += 1
        head = dummy_odd.next
        odd.next = dummy_even.next
        return head


sol = Solution()
head = utils.array_to_linked_list([1, 2, 3, 4, 5])
new = sol.oddEvenList(head)
print(new.val)
