# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        arr=[]
        if root is None : 
            return arr 
        st=[] 
        curr=root 
        while curr is not None : 
            st.append(curr) 
            curr=curr.left 
        while len(st)>0 : 
            curr=st.pop() 
            arr.append(curr.val) 
            curr=curr.right 
            while curr is not None : 
                st.append(curr) 
                curr=curr.left 
        return arr