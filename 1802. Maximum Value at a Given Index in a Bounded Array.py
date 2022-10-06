class Solution:
    def partial(self, x):
        return x * (x + 1) // 2
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(num):
            r = n - index - 1 # number of elements on the right
            l = index # number of elements on the left
            count = num
            if num <= l + 1:
                count += self.partial(num - 1) + l - num + 1
            else:
                count += self.partial(num - 1) - self.partial(num - l - 1)

            if num <= r + 1:
                count += self.partial(num - 1) + r - num + 1
            else:
                count += self.partial(num - 1) - self.partial(num - r - 1)

            return count <= maxSum
        
        left, right = 1, maxSum
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        if check(left):
            return left
        
        return left - 1

# Idea: create a function that takes a number x, and determines if it is possible for x to be placed at index. With this function,
#  perform a binary search with bounds starting at (0, maxSum). If the midpoint can be placed at index, move the left pointer. 
# If it can't, move the right pointer.
# So how do we check for a given number x? Greedily minimize the array's sum. First, place the number at the index.
#  Then, on both the left and right side, start counting down from that number. For example, with n = 7, index = 4, 
# if we wanted to place a 10, our optimal array would look like [6, 7, 8, 9, 10, 9, 8]. To do the calculations, 
# we can use the partial sums of this infinite series.

# If there are more elements on one side than the number we are placing, then we'll end up with extra 1s. 
# For example, [1, 1, 1, 2, 1] from placing the 2. So, our total will be the partial sum of x - 1 + the extra 1s.

# If there are less elements on one side than the number we are placing, then we can still take the partial sum of x - 1, 
# and then subtract from that the partial sum of the difference x - number of elements - 1. 
# For example, with [6, 7, 8, 9, 10, 9, 8], the total from the left is equal to the (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9) - (1 + 2 + 3 + 4 + 5), 
# which is the partial sum with 9 - the partial sum with 10 - 4 - 1 = 5.
# This gives us a constant time check for if a given number can satisfy the conditions.
# Time complexity is O(log(maxSum)) - the check function runs in constant time, so its just a quick binary search.
# Space complexity is O(1)