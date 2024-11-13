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

    def Levelorder(self, root):
        if not root:
            return []
        res = [root.val]
        queue = [root]
        count = 0
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    res.append(node.right.val)
            count += 1

        return res, count - 1


solution = Solution()
root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = solution.create_tree(root_list)
print(solution.Levelorder(root))
