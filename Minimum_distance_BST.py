# Definition for a binary tree node.
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
        res = [root.val]
        res.extend(self.preorder(root.left))
        res.extend(self.preorder(root.right))
        return res

    def minDiffInBST(self, res):
        res = self.preorder(root)
        res.sort()
        min_dist = float("inf")
        for i in range(1, len(res)):
            min_dist = min(min_dist, res[i] - res[i - 1])
        return min_dist


solution = Solution()
root_list = [27, None, 34, None, 58, 50, None, 44]
root = solution.create_tree(root_list)
# res = solution.preorder(root)
print(solution.minDiffInBST(root))
