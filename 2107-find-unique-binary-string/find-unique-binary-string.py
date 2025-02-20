class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str: 
        def generate_binary(n, s, a) : 
            if n==0 : 
                a.append(s)
                return None
            generate_binary(n-1, s+"0", a)
            generate_binary(n-1, s+"1", a) 
        n=len(nums)
        s="" 
        a=[]
        generate_binary(n, s, a)
        nums=set(nums) 
        for i in a : 
            if i not in nums : 
                return i