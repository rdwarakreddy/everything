class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_tree(root_list):
    if not root_list:
        return None
    root = TreeNode(root_list[0])
    queue = [root]
    i = 1
    while i < len(root_list):
        current = queue.pop(0)
        if root_list[i] is not None:
            current.left = TreeNode(root_list[i])
            queue.append(current.left)
        i += 1

        if i < len(root_list) and root_list[i] is not None:
            current.right = TreeNode(root_list[i])
            queue.append(current.right)
        i += 1
    return root


def inorderTraversal(root):
    if root is None:
        return []
    res = []
    res.extend(inorderTraversal(root.left))
    res.append(root.value)
    res.extend(inorderTraversal(root.right))
    return res


root_list = [10, 5, 20, 3, 7, 15, 25]
root = create_tree(root_list)
print(inorderTraversal(root))
