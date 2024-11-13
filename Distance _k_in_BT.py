from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
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

    def find_parents(self, root, parentMap):
        if root is None:
            return
        if root.left:
            parentMap[root.left] = root
            self.find_parents(root.left, parentMap)
        if root.right:
            parentMap[root.right] = root
            self.find_parents(root.right, parentMap)

    def findDistance(self, root, target, k):
        # Create a dictionary with parent and child nodes
        parentMap = {}
        self.find_parents(root, parentMap)

        # Perform BFS from target node
        queue = deque(
            [(target, 0)]
        )  # Initialize queue with the target node and distance 0
        visited = set([target])  # Mark the target node as visited
        result = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.value)
            # Add left, right, and parent node to the queue if not visited
            for neighbor in (node.left, node.right, parentMap.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return result


# Example usage
root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
solution = Solution()
root = solution.create_tree(root_list)
target_node = 5  # Example: target is the node with value 5
print(solution.findDistance(root, target_node, 2))
