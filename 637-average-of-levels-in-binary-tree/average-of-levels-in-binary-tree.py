# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
from collections import defaultdict 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]: 
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
            arr.append(sum(temp)/len(temp)) 
        return arr 