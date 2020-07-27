# Solution 1
def two_number_sum(array, target_sum):
	for i in range(len(array) - 1):
		x = array[i]
		for j in range(i+1, len(array)):
			y = array[j]
			if x+y == target_sum:
				return [x, y]
	return []

# Solution 2
def two_number_sum_second(array, target_sum):
	nums = {}
	for num in array:
		difference = target_sum - num
		if difference in nums:
			return [difference, num]
		else:
			nums[num] = True
	return []

# Solution 3
def two_number_sum_third(array, target_sum):
	array.sort()
	left = 0
	right = len(array)-1
	while left != right:
		test_sum = array[left] + array[right]
		if test_sum == target_sum:
			return [array[left], array[right]]
		elif test_sum < target_sum:
			left += 1
		else: 
			right -= 1
	return []
