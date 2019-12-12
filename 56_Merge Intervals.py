class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        if len(intervals)==0: return []
        
        intervals.sort()
        res.append(intervals[0])
        for i in range (1, len(intervals)):
            
            inter=res.pop()
            if intervals[i][0]>inter[1]:
                res.append(inter)
                res.append(intervals[i])
                
            if intervals[i][0]<=inter[1] and intervals[i][1]>=inter[1]:
                res.append([inter[0], intervals[i][1]])
                
            
            if intervals[i][0]<=inter[1] and intervals[i][1]<inter[1]:
                res.append([inter[0], inter[1]])
                
        return res
            
            
            
            
            
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key= lambda x: x[0])
        
        length=len(intervals)
        
        res=[]
        
        for i in range (length):
            if res==[]:
                res.append(intervals[0])
                
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1], intervals[i][1])
                
            else:
                res.append(intervals[i])
        return res  
