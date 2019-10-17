class Solution:
    def reverseWords(self, s: str) -> str:
        s_=s.split()[::-1]
        return ' '.join(s_)
        
