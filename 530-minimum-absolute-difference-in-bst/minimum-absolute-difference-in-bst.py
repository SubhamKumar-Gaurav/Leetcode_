# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[] 
        def inorder(node) : 
            if node : 
                inorder(node.left) 
                arr.append(node.val) 
                inorder(node.right) 
        
        inorder(root) 
        arr.sort() 
        ans=float("inf")
        for i in range(1, len(arr)) : 
            ans=min(ans, abs(arr[i-1]-arr[i])) 
        return ans 