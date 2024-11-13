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

    def preorder(self, root):
        if root is None:
            return []
        res = [root.value]
        res.extend(self.preorder(root.left))
        res.extend(self.preorder(root.right))
        return res

    def inorder(self, root):
        if root is None:
            return []
        res = []
        res.extend(self.inorder(root.left))
        res = [root.value]
        res.extend(self.inorder(root.right))
        return res


solution = Solution()
root_list = [10, 5, 20, 3, 7, 15, 25]
root = solution.create_tree(root_list)
print(solution.inorder(root))
