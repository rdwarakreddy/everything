from collections import deque, defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def create_tree(self, root_list):
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

    def VerticalOrder(self, root):
        coloumns = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, col = queue.popleft()
            coloumns[col].append((node, row))
            if node.left is not None:
                queue.append([node, row + 1, col - 1])
            if node.right is not None:
                queue.append([node, row + 1, col + 1])
        return coloumns


solution = Solution()
root_list = [3, 9, 20, None, None, 15, 7]
root = solution.create_tree(root_list)
print(solution.VerticalOrder(root))
