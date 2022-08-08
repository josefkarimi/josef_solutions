"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recive(root):
            if root :
                out.append(root.val)
                for item in root.children:
                    recive(item)
                    
        out = []
        recive(root)
        return out



# Runtime: 78 ms, faster than 54.74% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.3 MB, less than 16.18% of Python3 online submissions for N-ary Tree Preorder Traversal.