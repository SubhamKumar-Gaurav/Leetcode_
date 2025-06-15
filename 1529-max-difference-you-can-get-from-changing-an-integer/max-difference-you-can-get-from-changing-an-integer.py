class Solution:
    def maxDiff(self, num: int) -> int: 
        nums=list(str(num)) 
        first=None   
        for i in range(len(nums)) : 
            if nums[i]!="9" : 
                first=nums[i] 
                break
        second=None 
        for i in range(len(nums)) :                 
            if nums[i]!="1" and nums[i]!="0" : 
                if i!=0 : 
                    second=nums[i] 
                    second_val="0"
                    break 
                else : 
                    second=nums[i]
                    second_val="1" 
                    break 

        max_val=""
        min_val=""
        if first is None : 
            res1=num
        else : 
            for i in range(len(nums)) : 
                if nums[i]==first : 
                    max_val+="9" 
                else : 
                    max_val+=nums[i]  
            res1=int(max_val)   

        if second is None : 
            res2=num 
        else : 
            for i in range(len(nums)) : 
                if nums[i]==second : 
                    min_val+=second_val 
                else : 
                    min_val+=nums[i] 
            res2=int(min_val)
        return res1-res2      