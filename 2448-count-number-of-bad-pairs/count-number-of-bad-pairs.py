class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        diff_arr=[]
        for i in range(n) : 
            diff_arr.append(i-nums[i]) 
        total=(n*(n-1))//2 
        good_pair={} 
        good=0
        for i in range(len(diff_arr)) : 
            if diff_arr[i] in good_pair : 
                good+=good_pair[diff_arr[i]] 
                good_pair[diff_arr[i]]+=1
            else :  
                good_pair[diff_arr[i]]=1
        return total-good