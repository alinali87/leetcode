class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        # iterate till index node
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.size == 0:
            self.head = new_node
            self.size += 1
            return
        node = self.head
        while node and node.next:
            node = node.next
        node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        node = self.head
        for _ in range(index - 1):
            node = node.next
        new_node = ListNode(val, node.next)
        node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        if index == 0 and self.size > 0:
            self.head = self.head.next
        else:
            prev = ListNode(None, self.head)
            node = self.head
            for _ in range(index):
                node = node.next
                prev = prev.next
            prev.next = node.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
