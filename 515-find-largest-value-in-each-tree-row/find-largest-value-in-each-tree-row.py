# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None : 
            return [] 
        
        arr=[]     
        q=deque()  
        q.append(root) 

        while q : 
            temp=[] 
            for i in range(len(q)) : 
                node=q.popleft() 
                temp.append(node.val) 

                if node.left : 
                    q.append(node.left) 
                if node.right : 
                    q.append(node.right) 
            arr.append(max(temp)) 
        return arr 