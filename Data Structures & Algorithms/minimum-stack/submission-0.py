class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        newMin = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None
