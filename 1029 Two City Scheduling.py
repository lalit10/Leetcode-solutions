class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_costs = len(costs) 
        N = len_costs //2  #N is the number of people in any city
        sum_A = 0
        diff_arr = [0] * len_costs  #Create an array to store the difference between the cost of A and B
        for i in range(len_costs):
            sum_A+= costs[i][0]  #Sum the cost of A
            diff_arr[i] = (costs[i][0]- costs[i][1])  #Store the difference between the cost of A and B in the array
        diff_arr.sort(reverse=True) #Sort the array in descending order
        return sum_A - sum(diff_arr[0:N])