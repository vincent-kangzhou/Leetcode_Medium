class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        def dfs(candidates, target, i, cur, ans):
            if target==0:
                ans.append(cur[:])
                return 
            
            for i in range (i, len(candidates)):
                if candidates[i]>target:return
                
                cur.append(candidates[i])
                
                dfs(candidates, target-candidates[i], i, cur, ans)
                
                cur.pop()
                
        candidates.sort()
        dfs(candidates, target, 0, [], ans)
            
        return ans
