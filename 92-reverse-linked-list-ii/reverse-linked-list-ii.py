# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        st1=[] 
        st2=[] 
        st3=[] 

        curr=head 
        i=1 
        while i<left and curr : 
            st1.append(curr.val) 
            curr=curr.next 
            i+=1 
        st1.reverse()
        
        while i>=left and i<=right and curr : 
            st2.append(curr.val) 
            curr=curr.next 
            i+=1 
        
        while i>right and curr : 
            st3.append(curr.val) 
            curr=curr.next 
            i+=1 
        st3.reverse()

        curr=head 
        for i in range(len(st1)) : 
            curr.val=st1.pop() 
            curr=curr.next 
        
        for j in range(len(st2)) : 
            curr.val=st2.pop() 
            curr=curr.next 
        
        for k in range(len(st3)) : 
            curr.val=st3.pop() 
            curr=curr.next
        
        return head 