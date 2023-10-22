from typing import List, Optional


class ListNode:
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.next = nxt


class MyHashMap:

    def __init__(self):
        self.size = 19991
        self.mult = 12582917
        self.map: List[Optional[ListNode]] = [None] * self.size

    def hash(self, key) -> int:
        return key * self.mult % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        address = self.hash(key)
        node = self.map[address]
        if node is None:
            self.map[address] = ListNode(key, value)
        else:
            self.map[address] = ListNode(key, value, self.map[address])

    def get(self, key: int) -> int:
        address = self.hash(key)
        node = self.map[address]
        if node is None:
            return -1
        if node.key == key: return node.value
        while node.next:
            if node.next.key == key:
                return node.next.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        address = self.hash(key)
        node = self.map[address]
        if node is None:
            return
        self.map[address] = self.remove_from_node(node, key)

    def remove_from_node(self, node: ListNode, key: int) -> Optional[ListNode]:
        if node is None:
            return None
        if node.key == key:
            return node.next
        head = node
        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                break
            else:
                prev = node
                node = node.next
        return head

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
