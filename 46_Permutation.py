class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==[]: return []
        if len(nums)==1: return [nums]
        res=[]
        for i in range(len(nums)):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
                
        return res
            
