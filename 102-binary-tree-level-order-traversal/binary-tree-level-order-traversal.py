# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root is None : 
            return res
        
        q=deque() 
        q.append(root) 

        while q : 
            same_level=[]
            for i in range(len(q)) : 
                node=q.popleft() 
                same_level.append(node.val) 

                if node.left : 
                    q.append(node.left) 
                if node.right : 
                    q.append(node.right) 
            res.append(same_level) 
        return res 