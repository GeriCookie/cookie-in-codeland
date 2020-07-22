# Solution 1
def two_number_sum(array, targetSum):
    for i in range(len(array) - 1):
		x = array[i]
		for j in range(i+1, len(array)):
			y = array[j]
			if x+y == targetSum:
				return [x, y]
	return []

# Solution 2
def two_number_sum(array, targetSum):
	nums = {}
	for num in array:
		difference = targetSum - num
		if difference in nums:
			return [difference, num]
		else:
			nums[num] = True
	return []

# Solution 3
def two_number_sum(array, targetSum):
    array.sort()
	left = 0
	right = len(array)-1
	while left != right:
		testSum = array[left] + array[right]
		if testSum == targetSum:
			return [array[left], array[right]]
		elif testSum < targetSum:
			left += 1
		else: 
			right -= 1
	return []
