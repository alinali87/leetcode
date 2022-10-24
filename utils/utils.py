def test(output, expected):
    assert output == expected, f'output: {output}, expected: {expected}'


def input_to_list(inp: str, sep=' ', cast_to=int) -> list:
    """Split the input string by separator and cast each value to cast_to type
       Return list of values of cast_to type
    """
    return list(map(cast_to, inp.split(sep)))


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(arr: list) -> ListNode:
    dummy = ListNode()
    node = dummy
    for v in arr:
        node.next = ListNode(v)
        node = node.next
    return dummy.next