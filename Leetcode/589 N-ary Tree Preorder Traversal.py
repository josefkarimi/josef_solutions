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