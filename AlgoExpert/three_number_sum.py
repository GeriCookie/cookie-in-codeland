def three_number_sum(array, targetSum):
	array.sort()
	result = []
    for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			testSum = array[i] + array[left] + array[right]
			if testSum == targetSum:
				result.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif testSum < targetSum:
				left += 1
			elif testSum > targetSum:
				right -= 1
	return result
		
