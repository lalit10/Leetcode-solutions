def minSubArrayLen(s, nums):
	res = float('inf')
	left, total = 0, 0
	
	for i in range(len(nums)):
		total += nums[i]
		while total >= s:
			res = min(res, i - left + 1)
			total -= nums[left]
			left += 1
	
	return res if res != float('inf') else 0