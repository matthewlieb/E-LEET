# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # if root is empty, return none
        if root is None:
            return None
        # if root has leaves, recursively run program to get to bottom node and evaluate
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # if no more leaves, check if value is target and delete if it is
        if (root.val == target and root.left is None and root.right is None):
            return None
        return root
