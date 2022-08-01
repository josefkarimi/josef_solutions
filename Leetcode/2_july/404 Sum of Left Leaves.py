# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.arr=[]
        def findleft(root):
            if not root :
                return
            if root.left and root.left.left is None and root.left.right is None :
                self.arr.append(root.left.val)
            findleft(root.left)
            findleft(root.right)
        findleft(root)
        #print (self.arr)
        return (sum(self.arr))



# Runtime: 47 ms, faster than 60.60% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.7 MB, less than 45.73% of Python3 online submissions for Sum of Left Leaves.