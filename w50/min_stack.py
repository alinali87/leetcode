class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# val = 3
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# print(param_3)
# param_4 = obj.getMin()
# print(param_4)
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())  #;    // return 0
print(minStack.getMin())  #; // return -2
