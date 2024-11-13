from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, we return None (no more nodes to process)
        if not preorder or not inorder:
            return None

        # Root node is the first element in the preorder list
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the root value in the inorder list to split into left and right subtrees
        mid = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


# Test case
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

# Solution instance
solution = Solution()

# Build the tree
tree = solution.buildTree(preorder, inorder)

# Print the tree in level-order to verify the output structure
print(tree)
