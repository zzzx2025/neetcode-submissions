class MinStack:

    def __init__(self):
        self.stack = []
        self.num = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.num = min(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.num = None
        else:
            self.num = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.num
