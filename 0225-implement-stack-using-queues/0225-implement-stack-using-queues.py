from collections import deque
class MyStack:

    def __init__(self):
        self.items=deque()

    def push(self, x: int) -> None:
        self.items.append(x)
        for _ in range(len(self.items)-1):
            self.items.append(self.items.popleft())

    def pop(self) -> int:
        if len(self.items)==0:
            return -1
        x=self.items.popleft()
        return x

    def top(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        if len(self.items)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()