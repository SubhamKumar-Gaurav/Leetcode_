
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int: 
        MOD=1000000007
        ans=0 
        nums.sort() 
        i=0 
        j=len(nums)-1 
        while i<=j : 
            if (nums[i]+nums[j])<=target : 
                ans+=1<<(j-i) 
                if ans>MOD : 
                    ans=ans%MOD
                i+=1 
            else : 
                j-=1 
                left=i 
                right=j 
                value=target-nums[left] 
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] <= value:
                        left = mid + 1
                    else:
                        right = mid
                r = left - 1
        return ans 