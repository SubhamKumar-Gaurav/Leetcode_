class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,s,e)  : 
            while s<e : 
                l[s], l[e] = l[e], l[s] 
                s+=1 
                e-=1 

        n=len(nums)
        k=k%n 
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1) 
        return nums 