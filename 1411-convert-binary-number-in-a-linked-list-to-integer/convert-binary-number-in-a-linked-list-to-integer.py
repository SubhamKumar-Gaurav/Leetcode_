# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int: 
        arr=[] 
        curr=head 
        while curr != None : 
            arr.append(curr.val) 
            curr=curr.next
        if len(arr)==1 : 
            return arr[0]
        ans=0 
        two=1
        for i in range(len(arr)-1, -1, -1) : 
            if arr[i]==1 : 
                ans+=two
            two=2*two 
        return ans