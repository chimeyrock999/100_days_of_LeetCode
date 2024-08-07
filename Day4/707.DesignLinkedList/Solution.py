class Node:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def __getNode__(self, index: int) -> Node:
        if self.size == 0 or index >= self.size:
            return None
        if index == 0:
            return self.head
        if index == self.size - 1:
            return self.tail
        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i+=1
        return curr


    def get(self, index: int) -> int:
        return self.__getNode__(index).val if self.__getNode__(index) else -1
        

    def addAtHead(self, val: int) -> None:
        newHead = Node(val, None, self.head)
        self.size += 1
        if self.size == 1:
            self.tail = newHead
            self.head = newHead
            return
        self.head.prev = newHead
        self.head = newHead

    def addAtTail(self, val: int) -> None:
        newTail = Node(val, self.tail, None)
        self.size += 1
        if self.size == 1:
            self.head = newTail
            self.tail = newTail
            return
        self.tail.next = newTail
        self.tail = newTail
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = self.__getNode__(index)
        prev = node.prev
        newNode = Node(val, prev, node)
        prev.next = newNode
        node.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0:
            return 
        if index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
                self.size = 0
                return
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        node = self.__getNode__(index)
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1