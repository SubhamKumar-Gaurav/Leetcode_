class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int: 
        ## if len<3 --> no subarray will be formed 
        if len(nums)<3 : 
            return 0 

        ## if len==3 : 
        ## two cases - i) if diff same : return 1 ;
        ##            ii) else : return 0 
        elif len(nums)==3 : 
            if nums[1]-nums[0] == nums[2]-nums[1] : 
                return 1 
            else : 
                return 0 
        
        # we iterate over the array until the curr_diff is same (and increase the count too), else we move forward and update the curr_diff 
        else : 
            count=0 
            curr_diff=nums[1]-nums[0] 
            curr_len=2 
            for i in range(2, len(nums)): 
                if nums[i]-nums[i-1] == curr_diff : 
                    curr_len+=1
                    if curr_len>=3 : 
                        count+=curr_len-2
                else : 
                    curr_len=2 
                    curr_diff=nums[i]-nums[i-1]  
            return count 