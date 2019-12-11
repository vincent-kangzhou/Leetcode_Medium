class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums=list(range(1, n+1))

        
        def dfs(nums, k):
            res=[]
            if k==0: return []
            if k==1:
                
                for i in nums:
                    res.append([i])
                return res
            
            for i in range(len(nums)-k+1):
                for j in dfs (nums[i+1:],max(k-1,1)):
                    res.append([nums[i]]+j)
                    
            return res
        return dfs(nums,k)
        
