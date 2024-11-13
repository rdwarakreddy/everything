class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def appendAtFirst(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def appendAtMiddle(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            if new_node.next is None:
                self.tail = new_node

        self.length += 1

    def Traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def SearchWithValue(self, value):  # search with value
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == value:
                print(index)
            temp_node = temp_node.next
            index += 1
        print("Not found")

    def SearchWithIndex(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return

        temp_node = self.head
        for i in range(index):
            temp_node = temp_node.next
        print(temp_node.value)

    def UpdateValue(self, index, value):
        temp_node = self.head
        for i in range(index):
            temp_node = temp_node.next
        temp_node.value = value

    def PopFirstElement(self):
        if self.head is None:
            print("No element here")
            return

        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next
            temp_node.next = None

        self.length -= 1
        print(temp_node.value)

    def PopLastElement(self):
        popped_node = self.tail
        temp_node = self.head
        if self.head is None:
            print("No element here")
            return

        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        print(popped_node.value)

    def RemoveWithIndex(self, index):
        temp_node = self.head
        for i in range(index - 1):
            temp_node = temp_node.next
        popped_node = temp_node.next
        temp_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        print(popped_node.value)


# Initialize the linked list without any initial value
new_linkedList = LinkedList()
new_linkedList.appendAtLast(10)
new_linkedList.appendAtLast(20)
new_linkedList.appendAtLast(30)
new_linkedList.appendAtMiddle(40, 3)
print(new_linkedList)
new_linkedList.RemoveWithIndex(3)
print(new_linkedList)
