class Solution(object):
    def levelOrder(self, root):
        d = collections.defaultdict(list)
        def function(root, k):
            if not root:
                return None
            d[k].append(root.val)
            left, right = function(root.left, k+1), function(root.right, k+1)
        function(root,0)
        p = []
        for i in d:
            p.append(d[i])
  
        return p



# Runtime: 59 ms, faster than 39.55% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.9 MB, less than 9.89% of Python3 online submissions for Binary Tree Level Order Traversal.