class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is in between p and q
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root
        
        # if p and q are to the left of root
        if root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if p and q are the right of root
        return self.lowestCommonAncestor(root.right, p, q)



# Runtime: 97 ms, faster than 77.06% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.8 MB, less than 68.62% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.