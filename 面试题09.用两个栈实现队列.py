class CQueue:

    def __init__(self):
        self.main_stack = []
        self.operation_stack = []

    def appendTail(self, value: int) -> None:
        self.main_stack.append(value)

    def deleteHead(self) -> int:
        val = -1
        if len(self.main_stack) > 0:
            while len(self.main_stack) > 1:
                self.operation_stack.append(self.main_stack.pop())
            val = self.main_stack.pop()
            while len(self.operation_stack) > 0:
                self.main_stack.append(self.operation_stack.pop())
        return val


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()