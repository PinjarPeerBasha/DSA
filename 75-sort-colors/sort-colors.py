class Solution(object):
    def sortColors(self, nums):
        low=0
        temp=0
        high=len(nums)-1

        while temp <= high:
            if nums[temp]==0:
                nums[low],nums[temp]=nums[temp],nums[low]
                low+=1
                temp+=1
            elif nums[temp]==1:
                temp+=1
            else:
                nums[temp],nums[high]=nums[high],nums[temp]
                high-=1
        
        return nums        