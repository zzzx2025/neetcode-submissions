class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        MyNode = Node(x)
        if self.head is None:
            self.head = MyNode
            self.tail = MyNode
        else:
            MyNode.prev = self.tail
            self.tail.next = MyNode
            self.tail = MyNode

    def pop(self) -> int:
        cur = self.tail
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = cur.prev
            self.tail.next = None
            cur.prev = None
        return cur.val

    def top(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()