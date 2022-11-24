class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #Overlap is the main difficulty
        #Start coordinates max and end coordinates min ye sab together with 0
        area_1 = (ay2-ay1) * (ax2-ax1)
        area_2 = (by2-by1) * (bx2-bx1)
        
        x_overlap = max(min(ax2,bx2) - max(ax1,bx1),0)
        y_overlap = max(min(ay2,by2) - max(ay1,by1),0)
        area_overlap = x_overlap * y_overlap
        
        return area_1 + area_2 - area_overlap
        