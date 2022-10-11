from collections import defaultdict
from heapq import *
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        heap = []
        for i in range(len(timestamp)):
            heapq.heappush(heap, (timestamp[i],website[i],username[i]))
        
        users = defaultdict(list)
        
        while heap:
            timeStamp,webSite,userName = heapq.heappop(heap)
            users[userName].append(webSite)
            
        count = defaultdict(int)
        maximum = 0
        result = tuple()
        
        for key in users:
            combos = combinations(users[key],3)
            for sequence in set(combos):
                count[sequence]+=1
                if count[sequence]>maximum:
                    maximum = count[sequence]
                    result = sequence              
                elif count[sequence]==maximum:
                    if sequence<result:
                        result = sequence
        return list(result)

#Another solution
# class Solution:
#     def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
#         # Create tuples as shown in description
# 		# The timestamps may not always be pre-ordered (one of the testcases)
# 		# Sort first based on user, then time (grouping by user)
# 		# This also helps to maintain order of websites visited in the later part of the solution
#         users = defaultdict(list)
# 	    # It is not necessary to use defaultdict here, we can manually create dictionaries too
		
#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):    
#             users[user].append(site)     # defaultdicts simplify and optimize code

#         patterns = Counter()   # this can also be replaced with a manually created dictionary of counts
		
# 		# Get unique 3-sequence (note that website order will automatically be maintained)
# 		# Note that we take the set of each 3-sequence for each user as they may have repeats
# 		# For each 3-sequence, count number of users
		
#         for user, sites in users.items():
#             patterns.update(Counter(set(combinations(sites, 3))))     
		
# 		# Re-iterating above step for clarity
# 		# 1. first get all possible 3-sequences combinations(sites, 3)
# 		# 2. then, count each one once (set)
# 		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter)) 
# 		# - updating a dictionary will update the value for existing keys accordingly (int in this case)
	
# 		# get most frequent 3-sequence sorted lexicographically
#         return max(sorted(patterns), key=patterns.get)