# #Using Tree
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# def preorder(root):
#     if root is None:
#         return []  # Return an empty list if the node is None
#     res = [root.value]
#     res.extend(preorder(root.left))  # Traverse left subtree
#     res.extend(preorder(root.right))  # Traverse right subtree
#     return res  # Make sure to return the result
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print("Pre-order Traversal:", preorder(root))

def preorder_traversal_from_list(tree):
    def preorder(index):
        if index >= len(tree) or tree[index] is None:
            return []
        
        # Visit root node
        result = [tree[index]]
        # Visit left subtree
        result.extend(preorder(2 * index + 1))
        # Visit right subtree
        result.extend(preorder(2 * index + 2))
        return result

    return preorder(0)

# Input: binary tree represented as a list
root = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

# Perform pre-order traversal
print("Pre-order Traversal:", preorder_traversal_from_list(root))

