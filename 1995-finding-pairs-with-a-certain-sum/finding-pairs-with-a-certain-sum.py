from collections import defaultdict 

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2 
        self.d=defaultdict(int) 
        for i in self.nums2 : 
            self.d[i]+=1 

    def add(self, index: int, val: int) -> None:
        if self.d[self.nums2[index]] >0 : 
            self.d[self.nums2[index]]-=1 
        self.d[self.nums2[index]+val]+=1
        self.nums2[index]+=val 


    def count(self, tot: int) -> int: 
        c=0 
        for i in range(len(self.nums1)) : 
            if tot-self.nums1[i] in self.d : 
                c+=self.d[tot-self.nums1[i]] 
        return c 


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)