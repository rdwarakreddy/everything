class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, value, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        temp_node = head
        current_node = head.next
        while current_node is not None:
            if current_node.value == value:
                temp_node.next = current_node.next
                current_node = current_node.next
            elif current_node.value == value and current_node.next is None:
                temp_node.next = None
            elif head.value == value:
                head = head.next

            else:
                temp_node = current_node
                current_node = current_node.next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print the linked list
def print_linked_list(head):
    current = head
    result = ""
    while current is not None:
        result += str(current.val)
        if current.next is not None:
            result += "->"
        current = current.next
    print(result)


values = [1, 1, 2]
linked_list = create_linked_list(values)
solution = Solution()
removeelement = solution.deleteDuplicates(6)
print(removeelement)
