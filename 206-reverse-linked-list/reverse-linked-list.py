# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLL(head) : 
            if head==None : 
                return head
            if head.next==None : 
                return head  
            restHead=reverseLL(head.next) 
            restTail=head.next 
            restTail.next=head 
            head.next=None 
            return restHead 
        return reverseLL(head)