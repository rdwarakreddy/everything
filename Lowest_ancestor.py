class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

    def findparent(self, root, parentMap=None):
        if root is None:
            return parentMap
        if parentMap is None:
            parentMap = {}
        if root.left is not None:
            parentMap[root.left] = root
            self.findparent(root.left, parentMap)
        if root.right is not None:
            parentMap[root.right] = root
            self.findparent(root.right, parentMap)
        return parentMap

    def lowestCommonAncestor(self, root, p, q):
        parentMap = self.findparent(root)
        ancestor_set = set()
        p_node = self.find_node(root, p)
        q_node = self.find_node(root, q)

        if not p_node or not q_node:
            return None
        while p_node is not None:
            ancestor_set.add(p_node)
            p_node = parentMap.get(p_node)
        while q_node is not None:
            if q_node in ancestor_set:
                return q_node
            q_node = parentMap.get(q_node)

        return None

    def find_node(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        left_search = self.find_node(root.left, val)
        if left_search:
            return left_search
        return self.find_node(root.right, val)


# Test case
solution = Solution()
root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = solution.create_tree(root_list)
p, q = 5, 1
lca = solution.lowestCommonAncestor(root, p, q)
if lca:
    print(lca.val)
