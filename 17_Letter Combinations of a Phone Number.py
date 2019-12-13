class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictMap={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        import itertools
        
        if len(digits)==0:return []
        res=dictMap[digits[0]]
        
        for i in range(1, len(digits)):
            tmp=[]
            for j in itertools.product(res, dictMap[digits[i]]):
                tmp.append(''.join(j))
                
            res=tmp
        return res
            
            
            
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictMap={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        import itertools
        
        if len(digits)==0:return []
        if len(digits)==1:
            return dictMap[digits[0]]
        
        res=[]
        
        for word in dictMap[digits[0]]:
            for ans in self.letterCombinations(digits[1:]):
                res.append(word+ans)
        return res
                
