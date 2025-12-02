# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

from collections import defaultdict 
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr=[] 
        def inorder(node) : 
            if node : 
                inorder(node.left) 
                arr.append(node.val)  
                inorder(node.right) 
        inorder(root) 
     
        def floor(arr, x) : 
            if x<arr[0] : 
                return -1 
            l=0 
            r=len(arr)-1 
            ceilVal=arr[0] 
            while l<=r : 
                mid=(l+r)//2 
                if arr[mid]==x : 
                    ceilVal=arr[mid] 
                    return ceilVal 
                elif arr[mid]>x : 
                    r=mid-1 
                else : 
                    ceilVal=arr[mid] 
                    l=mid+1 
            return ceilVal 
        
        def ceil(arr, x) : 
            if x>arr[-1] : 
                return -1 
            l=0 
            r=len(arr)-1 
            ceilVal=arr[-1] 
            while l<=r : 
                mid=(l+r)//2 
                if arr[mid]==x : 
                    ceilVal=arr[mid] 
                    return ceilVal 
                elif arr[mid]<x : 
                    l=mid+1 
                else : 
                    ceilVal=arr[mid] 
                    r=mid-1 
            return ceilVal
        
        ans=[] 
        for q in queries : 
            ans.append([floor(arr, q), ceil(arr, q)]) 
        return ans 