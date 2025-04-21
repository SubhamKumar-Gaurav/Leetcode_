
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int: 
        curr=0 
        minVal=0 
        maxVal=0 
        for d in differences : 
            curr+=d 
            minVal=min(minVal, curr) 
            maxVal=max(maxVal, curr) 
            if ((upper-maxVal)-(lower-minVal)+1)<=0 : 
                return 0 
        return (upper-maxVal)-(lower-minVal)+1