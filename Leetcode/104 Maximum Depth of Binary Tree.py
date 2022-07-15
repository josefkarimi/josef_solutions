# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    


# Runtime: 70 ms, faster than 38.76% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.2 MB, less than 74.78% of Python3 online submissions for Maximum Depth of Binary Tree.