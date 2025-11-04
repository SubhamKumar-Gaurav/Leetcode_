from collections import Counter 
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]: 
        n=len(nums) 
        arr=[] 
        for i in range(n-k+1) : 
            sub=nums[i:i+k] 
            freq=Counter(sub)
            sorted_elements=sorted(freq.items(), key=lambda y: (-y[1], -y[0])) 
            top_x_elements=sorted_elements[:x]  
            sub_sum=sum(value*count for value, count in top_x_elements) 
            arr.append(sub_sum) 
        return arr