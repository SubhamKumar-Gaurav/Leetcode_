# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        def reverseLL(head) : 
            curr=head 
            prev=None 
            while curr : 
                next_node=curr.next 
                curr.next=prev 
                prev=curr 
                curr=next_node 
            return prev 

        l1=reverseLL(l1) 
        l2=reverseLL(l2) 

        s1="" 
        s2=""
        curr=l1 
        while curr : 
            s1+=str(curr.val) 
            curr=curr.next 
        curr=l2 
        while curr : 
            s2+=str(curr.val) 
            curr=curr.next 

        ans=int(s1)+int(s2) 
        s_ans=str(ans) 
        head=ListNode(int(s_ans[0])) 
        curr=head 
        for i in range(1,len(s_ans)) : 
            curr.next=ListNode(int(s_ans[i])) 
            curr=curr.next 
        return reverseLL(head)