# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def revLL(head) :  # Reversing LL 
            curr=head 
            prev=None 
            while curr : 
                next_node=curr.next
                curr.next=prev 
                prev=curr 
                curr=next_node 
            return prev 
        if head==None : 
            return True  
        slow=head 
        fast=head 
        while fast and fast.next : 
            slow=slow.next 
            fast=fast.next.next
        rev=revLL(slow) 
        while rev: 
            if rev.val!=head.val : 
                return False 
            rev=rev.next 
            head=head.next 
        return True 