# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        arr=[] 
        def inorder(node) : 
            if node : 
                inorder(node.left) 
                arr.append(node.val) 
                inorder(node.right) 
        
        inorder(root1) 
        inorder(root2) 
        arr.sort() 
        return arr