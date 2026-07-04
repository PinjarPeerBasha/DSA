class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if k < 0:
            k +=len(nums)
        
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
     

    def reverse(self,nums,left,right):
        while left < right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        