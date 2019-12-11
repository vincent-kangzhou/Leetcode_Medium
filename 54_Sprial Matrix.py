class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix ==[[]] or matrix==[]:
            return []
        
        m=len(matrix)
        n=len(matrix[0])
        res=[]
        if m==1:
            return matrix[0]
        
        if n==1:
            return [matrix[i][0] for i in range(m)]
        
        res=matrix[0]+[matrix[i][-1] for i in range(1,m-1)]+matrix[-1][::-1]+[matrix[i][0] for i in range(m-2,0,-1)]
        sub_res=[]
        if m>2 and n>2:
            for i in range(1,m-1):
                sub_res.append(matrix[i][1:n-1])
            
        for j in self.spiralOrder(sub_res):
            res.append(j)
            
        return res
