from typing import List, Optional

def make_linked_list(lst):
    if len(lst) == 0:
        return None
    node = ListNode(lst[0])
    head = node
    for value in lst[1:]:
        node.next = ListNode(value)
        node = node.next
    return head


def find_min(lists):
    min_i = 0
    min_node = ListNode(float('inf'))
    for i in range(len(lists)):
        if lists[i] is not None:
            if lists[i].val < min_node.val:
                min_node = lists[i]
                min_i = i
    return min_node, min_i

def lists_to_linked_list(result):
    if len(result) == 0:
        return None
    node = result[0]
    head = node
    for i in range(1, len(result)):
        node.next = result[i]
        node = node.next
    return head




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    result = []
    if len(lists) < 1:
        return None
    while len(lists) > 0:
        min_node, i = find_min(lists)
        try:
            lists[i] = lists[i].next
        except AttributeError:
            pass
        if lists[i] is None:
            lists.pop(i)
        min_node.next = None
        # if len(result) > 0:
        #     result[-1].next = min_node
        result.append(min_node)
    result = lists_to_linked_list(result)
    return result




if __name__ == "__main__":
    a = make_linked_list([1, 4, 5])
    b = make_linked_list([1, 3, 4])
    c = make_linked_list([2, 6])
    d = make_linked_list([])
    lists = [a, b, c]
    print(mergeKLists(lists))

