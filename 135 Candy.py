class Solution:
    def candy(self, ratings: List[int]) -> int:
        #Assign 1 initially
        # Check from left to right and right to left
        arr = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1]+1
        #result = arr[len(ratings)-1]
        for i in range(len(ratings)-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i+1]+1, arr[i])  # Changed this due to failing testcase and referred to various solutions
            #result +=arr[i]
        #print("Result is:-", result)
        return sum(arr)

# Time Complexity: O(N)
# Space Complexity: O(N)

#We'll start with a list the size of the queue and filled with one since every child needs to get at least one candy.
#Then, moving from left to right, beginning with the second index, we assess whether the current kid has a higher rating than the prior one.If this is the case, we will increase the candies given to the current child by the amount given to the prior child plus one.
#In a subsequent iteration, we traverse the ratings from right to left, beginning with the second index from the last and testing if the current rating is higher than the previous one.If this is the case, the current kid's index in the candy list is updated by the maximum of the current rating or what the prior child receives plus one.