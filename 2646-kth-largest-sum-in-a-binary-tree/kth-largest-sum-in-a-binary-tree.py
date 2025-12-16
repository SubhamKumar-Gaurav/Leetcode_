# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution: 
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int: 
        q=deque() 
        q.append(root) 
        arr=[] 
        i=0 

        while q : 
            temp=[] 
            for i in range(len(q)) : 
                node=q.popleft() 
                temp.append(node.val) 

                if node.left : 
                    q.append(node.left) 
                if node.right : 
                    q.append(node.right) 
            i+=1 
            arr.append([sum(temp), i]) 
        
        arr.sort(reverse=True) 
        
        if k>len(arr) : 
            return -1 
        return arr[k-1][0] 