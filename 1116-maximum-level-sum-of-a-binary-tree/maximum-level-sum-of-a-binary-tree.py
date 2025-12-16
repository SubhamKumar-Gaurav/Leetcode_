# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: 
        q=deque() 
        q.append(root) 
        arr=[] 

        while q : 
            temp=[] 
            for i in range(len(q)) : 
                node=q.popleft() 
                temp.append(node.val) 

                if node.left : 
                    q.append(node.left) 
                if node.right : 
                    q.append(node.right) 
                
            arr.append(sum(temp)) 
        
        idx=1 
        maxVal=arr[0] 
        for i in range(1, len(arr)) : 
            if arr[i]>maxVal : 
                maxVal=arr[i]
                idx=i+1 
        return idx 