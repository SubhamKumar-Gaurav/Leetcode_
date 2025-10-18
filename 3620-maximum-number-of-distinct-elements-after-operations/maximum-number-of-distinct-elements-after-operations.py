class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int: 
        nums.sort()  
        distinctCount=0 
        prevMax=float("-inf") 

        for  i in nums : 
            lowerBound=i-k 
            upperBound=i+k 
            if prevMax<lowerBound : 
                prevMax=lowerBound 
                distinctCount+=1 
            elif prevMax<upperBound : 
                prevMax+=1 
                distinctCount+=1 
        return distinctCount 

# Intuition: 
#   1) if the prev no. is less than nums[i]-k, then make it equal to nums[i]-k 
#   2) if the prev no. is greater then nums[i]-k and less than nums[i]+k, i.e. lie in the available range, then simply increase it by 1 
#   3) if the prev no. lie above nums[i]+k, then simply ignore it, we can't do anything to that number