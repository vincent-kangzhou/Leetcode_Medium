class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=bisect.bisect_left(nums,target)
        right=bisect.bisect_right(nums, target)
        if left==right:
            return [-1,-1]
        return [left, right-1]
        
        
        
        
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=0
        for i in range(len(nums)):
            if nums[i]==target:
                if count==0:
                    start=i
                    count+=1
                else:
                    count+=1
            elif count>0:
                break
        return [start, start+count-1] if count>0 else [-1,-1]
