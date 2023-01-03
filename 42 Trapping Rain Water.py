class Solution:
    def trap(self, height: List[int]) -> int:
        #Volume at ith position is min(left,right)- height[i]
        #Breaking it into seperate for left and right pointers
        #For left use i , right j
        if len(height) <=2:
            return 0
        vol = 0
        left,right = height[0], height[-1]
        i,j = 0 , len(height)-1
        while i <= j:
            if height[i] > left:
                left = height[i]
            if height[j] > right:
                right = height[j]
            
            if left < right:
                vol = vol+ left - height[i]
                i+=1
            else:
                vol = vol + right - height[j]
                j-=1
        return vol

