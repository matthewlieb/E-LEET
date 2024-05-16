# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        # if current node is leaf, return boolean of its value
        if root.left is None and root.right is None:
            return bool(root.val)
        # recursively evaluate the left and right subtrees
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        # if current node value is 2, perform an OR; otherwise perform an AND
        if root.val == 2:
            return left_val or right_val
        else:
            return left_val and right_val


## This code is O(n), where n is the number of nodes in the binary tree. The evaluateTree function visits each node onl once to perform its evaluation.
