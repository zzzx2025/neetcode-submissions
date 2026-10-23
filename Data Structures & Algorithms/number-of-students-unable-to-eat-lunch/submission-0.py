class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        for i in range(len(students)):
            node = Node(students[i])
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.size += 1
        
        
        for i in range(len(sandwiches)):   
            cur = self.head 
            count = 0
            while (self.head is not None):
                if self.head.val == sandwiches[i]:
                    self.head = self.head.next
                    cur = self.head
                    self.size -= 1
                    count = 0
                    break
                else:
                    self.tail.next = self.head
                    self.tail = self.head
                    self.head = self.head.next
                    cur = self.head
                    self.tail.next = None
                    count += 1
                if count >= self.size:
                    return self.size


        return self.size

