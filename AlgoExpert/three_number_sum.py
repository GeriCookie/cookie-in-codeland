def three_number_sum(array, target_sum):
	array.sort()
	result = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			testSum = array[i] + array[left] + array[right]
			if testSum == target_sum:
				result.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif testSum < target_sum:
				left += 1
			elif testSum > target_sum:
				right -= 1
	return result
		
