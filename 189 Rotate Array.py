class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """     
        '''
        Array reverse maar
        Fir usmei k pe break karke reverse kia
        Uske baad pehle left side and then right side k pe swap
        '''
        '''
        arr = [0 for i in range(len(nums))]        
        for i in range(len(nums)):
            arr[(i+k)%len(nums)] = nums[i] 

        for i in range(len(nums)):
            nums[i] = arr[i]
        '''
        k %= len(nums)  #When K is greater than L
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)
        
    def reverse(self, nums, left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left+=1
            right-=1
            
            