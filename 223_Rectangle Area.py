class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if E>=C or B>=H or F>=D or A>=G:
            return (D-B)*(C-A)+(H-F)*(G-E)
        width=min(G, C)-max(E,A)
        height=min(D, H)-max(F,B)
        
        return (D-B)*(C-A)+(H-F)*(G-E)-width*height
        
        
        
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        left=max(A,E)
        right=max(min(C,G),left)
        
        bottom=max(B,F)
        top=max(min(D,H),bottom)
        
        return (C-A)*(D-B)+(G-E)*(H-F)-(right-left)*(top-bottom)
        
