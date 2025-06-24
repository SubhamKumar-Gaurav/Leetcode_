class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]: 
        res=set() 
        for i in range(len(nums)) : 
            for j in range(len(nums)) : 
                if nums[i]==key and abs(i-j)<=k : 
                    res.add(i)
                    res.add(j) 
        arr=[] 
        for i in res : 
            arr.append(i)
        arr.sort() 
        return arr