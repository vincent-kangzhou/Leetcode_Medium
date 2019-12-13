class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=''
        thousand=num//1000
        num=num-thousand*1000
        
        for i in range(thousand):
            ans+='M'
            
        hundred=num//100
        num=num-hundred*100
        
        if hundred==5:
            ans+='D'
        elif hundred>5:
            if hundred==9:
                ans+='CM'
            else:
                ans+='D'
                for i in range(5, hundred):
                    ans+='C'
                    
        elif hundred<=4:
            if hundred==4:
                ans+='CD'
                
            else:
                for i in range(hundred):
                    ans+='C'
        tenth=num//10
        num=num-tenth*10
        if tenth==5:
            ans+='L'
        elif tenth>5:
            if tenth==9:
                ans+='XC'
            else:
                ans+='L'
                for i in range(5, tenth):
                    ans+='X'
                    
        elif tenth<=4:
            if tenth==4:
                ans+='XL'
            else:
                for i in range(tenth):
                    ans+='X'
                    
        if num==5:
            ans+='V'
        elif num>5:
            if num==9:
                ans+='IX'
            else:
                ans+='V'
                for i in range(5, num):
                    ans+='I'
                    
        elif num<=4:
            if num==4:
                ans+='IV'
            else:
                for i in range(num):
                    ans+='I'
                    
        return ans
            
        
        
        
        
