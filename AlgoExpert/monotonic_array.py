def is_monotonic(array):
	non_increasing = True
	non_decreasing = True
	for index in range(len(array)-1):
		if array[index] > array[index+1]:
			non_decreasing = False
		elif array[index] < array[index+1]:
			non_increasing = False
		if non_increasing == False and non_decreasing == False:
			return False
	return non_increasing or non_decreasing
