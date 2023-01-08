class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        
        def calc_slope(p1,p2):
            x1,y1 = p1
            x2,y2 = p2

            if x1==x2:
                return float('inf')
            return (y2-y1)/(x2-x1)
        
        res = 0
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1:]):
                slope = calc_slope(p1, p2)
                slopes[slope] += 1
                res = max(slopes[slope], res)
        return res+1
