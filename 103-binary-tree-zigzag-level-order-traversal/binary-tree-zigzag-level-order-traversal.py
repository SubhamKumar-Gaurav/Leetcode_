# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if root is None : 
            return [] 
        arr=[] 
        q=deque() 
        q.append(root) 
        j=0 
        while q : 
            temp=[] 
            for i in range(len(q)) :  
                node=q.popleft() 
                temp.append(node.val) 

                if node.left : 
                    q.append(node.left) 
                if node.right : 
                    q.append(node.right) 
            if j%2 : 
                arr.append(temp[::-1]) 
            else : 
                arr.append(temp) 
            j+=1 
        return arr 