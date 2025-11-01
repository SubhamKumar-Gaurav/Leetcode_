

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        n=-1 
        for i in nums : 
            n=max(i, n) 
        
        arr=[False for _ in range(n+1)] 

        for i in nums : 
            arr[i]=True 
        
        temp=ListNode() 
        curr=temp

        while head : 
            if head.val>=len(arr) or arr[head.val]==False :  
                curr.next=head 
                curr=curr.next 
            head=head.next 
        curr.next=None 
        return temp.next 