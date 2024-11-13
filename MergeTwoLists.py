class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class FirstLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result1 = []
        while temp_node is not None:
            result1.append(temp_node.value)
            temp_node = temp_node.next
        return ",".join(map(str, result1))

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


class SecondLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result2 = []
        while temp_node is not None:
            result2.append(temp_node.value)
            temp_node = temp_node.next
        return ",".join(map(str, result2))

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ThirdLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result3 = []
        while temp_node is not None:
            result3.append(temp_node.value)
            temp_node = temp_node.next
        return ",".join(map(str, result3))

    def mergeList(self, list1, list2):
        firstHead = list1.head
        secondHead = list2.head
        list3 = ThirdLinkedList()

        while firstHead and secondHead:
            if firstHead.value < secondHead.value:
                list3.appendAtLast(firstHead.value)
                firstHead = firstHead.next
            elif firstHead.value > secondHead.value:
                list3.appendAtLast(secondHead.value)
                secondHead = secondHead.next
            else:  # If both values are equal
                list3.appendAtLast(firstHead.value)
                list3.appendAtLast(secondHead.value)
                firstHead = firstHead.next
                secondHead = secondHead.next

        # Append remaining elements of list1 to list3
        while firstHead:
            list3.appendAtLast(firstHead.value)
            firstHead = firstHead.next

        # Append remaining elements of list2 to list3
        while secondHead:
            list3.appendAtLast(secondHead.value)
            secondHead = secondHead.next

        return list3

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


# Initialize the two linked lists and append elements
list1 = ThirdLinkedList()
list2 = ThirdLinkedList()
list1.appendAtLast(1)
list1.appendAtLast(2)
list1.appendAtLast(4)
list2.appendAtLast(1)
list2.appendAtLast(3)
list2.appendAtLast(4)

# Merge list1 and list2 into list3
list3 = ThirdLinkedList()
list3 = list3.mergeList(list1, list2)

# Print the merged list (list3)
print("Merged List:", list3)
