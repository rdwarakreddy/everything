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
            return None
        res = []
        queue = [root]
        while queue:
            qlen = len(queue)
            if queue[0] is not None:
                res.append(queue[0].val)
            if qlen > 1 and queue[-1] is not None:
                res.append(queue[-1].val)
            for i in range(qlen):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return res


solution = Solution()
root_list = [20, 10, 30, None, 15, None, 40, None, 17]
root = solution.create_tree(root_list)
print(solution.Levelorder(root))
