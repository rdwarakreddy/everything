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


new_linkedList = LinkedList()
new_linkedList.appendAtLast(1)
new_linkedList.appendAtLast(2)
new_linkedList.appendAtLast(3)
new_linkedList.appendAtLast(4)
new_linkedList.appendAtLast(5)
print(new_linkedList)
print(reversed(new_linkedList))
