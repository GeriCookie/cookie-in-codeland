# Solution 1
import sys
def smallest_difference(array_one, array_two):
	array_one.sort()
	array_two.sort()
	absolute_value = sys.maxsize
	result = []
	for num_one in array_one:
		for num_two in array_two:
			value = abs(num_one - num_two)
			if value <= absolute_value:
				absolute_value = value
				result = [num_one, num_two]
			elif value > absolute_value:
				continue
	return result
		
# Solution 2
def smallest_difference_second(array_one, array_two):
	array_one.sort()
	array_two.sort()
	index_one = 0
	index_two = 0
	absolute_value = sys.maxsize
	result = []
	test_value = 0
	while index_one < len(array_one) and index_two < len(array_two):
		number_one = array_one[index_one]
		number_two = array_two[index_two]
		test_value = abs(number_one - number_two)
		if number_one < number_two:
			index_one += 1
		elif number_one > number_two:
			index_two += 1
		elif number_one == number_two:
			return [number_one, number_two]
		
		if test_value < absolute_value:
			absolute_value = test_value
			result = [number_one, number_two]
			
	return result
		
		
