class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a,b,c,d=rec1[0],rec1[1],rec1[2],rec1[3]
        e,f,g,h=rec2[0],rec2[1],rec2[2],rec2[3]
        x1=max(a,e)
        y1=max(b,f)
        x2=min(c,g)
        y2=min(d,h)
        if ((x1<x2) and (y1<y2)):
            return True
        return False 