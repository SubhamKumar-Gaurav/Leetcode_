# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : 
            return 0 
        
    
        def height(root) : 
            if root is None : 
                return 0 
            else : 
                lHeight=height(root.left) 
                rHeight=height(root.right) 
                if lHeight>rHeight : 
                    return lHeight+1 
                else : 
                    return rHeight+1 
        return height(root) 