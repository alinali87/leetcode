# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_values(head: Optional[ListNode]) -> list:
    if head is None:
        return None
    res = [head.val]
    node = head
    while node.next:
        res.append(node.next.val)
        node = node.next
    return res


def array_to_list(lst):
    if len(lst) == 0:
        return None
    node = ListNode(lst[0])
    head = node
    for value in lst[1:]:
        node.next = ListNode(value)
        node = node.next
    return head


def find_min(heads) -> ListNode:
    min_ind = 0
    min_node = heads[0]
    for i in range(1, len(heads)):
        if heads[i].val < min_node.val:
            min_node = heads[i]
            min_ind = i
    if heads[min_ind].next is not None:
        heads[min_ind] = heads[min_ind].next
    else:
        heads.pop(min_ind)
    return min_node


def make_links(result):
    if len(result) == 0:
        return None
    node = result[0]
    head = node
    for i in range(1, len(result)):
        node.next = result[i]
        node = node.next
    return head


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # remove empty lists
        for i in range(len(lists) - 1, -1, -1):
            if lists[i] is None:
                lists.pop(i)
        if len(lists) < 1:
            return None
        result = []
        while len(lists) > 0:
            min_node = find_min(lists)
            min_node.next = None
            result.append(min_node)
        result = make_links(result)
        return result


# test
def test_1():
    s = Solution()
    a = array_to_list([1, 4, 5])
    b = array_to_list([1, 3, 4])
    c = array_to_list([2, 6])
    lists = [a, b, c]
    assert list_to_values(s.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_2():
    s = Solution()
    a = array_to_list([])
    b = array_to_list([])
    lists = [a, b]
    assert s.mergeKLists(lists) is None


if __name__ == "__main__":
    # test_1()
    test_2()

