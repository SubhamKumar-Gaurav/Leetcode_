# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        l=[] 
        curr=head 
        while curr : 
            l.append(curr.val) 
            curr=curr.next 
        
        maxVal=l[-1] 
        newArr=[l[-1]] 
        for i in range(len(l)-2, -1, -1) : 
            if l[i]>=maxVal : 
                newArr.append(l[i]) 
                maxVal=l[i] 

        newArr=newArr[::-1]  
        curr=head 
        for i in range(len(newArr)-1) :  
            curr.val=newArr[i] 
            curr=curr.next    
        curr.val=newArr[-1]  
        curr.next=None 
        return head 