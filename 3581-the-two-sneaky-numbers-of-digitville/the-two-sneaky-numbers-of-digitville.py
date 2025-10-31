class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr=[] 
        s=set()
        for i in nums : 
            if nums.count(i)==2 : 
                s.add(i) 
        for i in s : 
            arr.append(i) 
        return arr