class MaxQueue:

    def __init__(self):
        self.queue = []
        self.maxValues = []

    def max_value(self) -> int:
        if len(self.maxValues) == 0:
            return -1
        return self.maxValues[0]

    def push_back(self, value: int) -> None:
        while len(self.maxValues) > 0 and self.maxValues[-1] < value:
            self.maxValues.pop()
        self.queue.append(value)
        self.maxValues.append(value)

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        value = self.queue.pop(0)
        if value == self.maxValues[0]:
            self.maxValues.pop(0)
        return value


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()