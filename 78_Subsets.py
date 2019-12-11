

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, k):
            res=[]
            if k==0:
                return [[]]
            if k==1:
                for i in nums:
                    res.append([i])

                return res
            if k==len(nums):
                return [nums]

            for i in range(len(nums)-k+1):
                for j in dfs(nums[i+1:],max(k-1,1)):
                    res.append([nums[i]]+j)

            return res

        ans=[]
        for i in range(len(nums)+1):
            for j in dfs(nums,i):
                ans.append(j)    
        return ans
