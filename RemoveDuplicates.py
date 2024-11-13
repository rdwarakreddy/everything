class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def RemoveDuplicates(self):
        temp_node = self.head
        current_node = temp_node.next
        while temp_node.next is not None:
            if temp_node.value == current_node.value:
                temp_node.next = current_node.next
                current_node = current_node.next
            else:
                temp_node = temp_node.next
                current_node = current_node.next


new_linkedList = LinkedList()
new_linkedList.appendAtLast(1)
new_linkedList.appendAtLast(1)
new_linkedList.appendAtLast(2)
# new_linkedList.appendAtLast(3)
# new_linkedList.appendAtLast(3)
print(new_linkedList)
new_linkedList.RemoveDuplicates()
print(new_linkedList)
